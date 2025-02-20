from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from copy import deepcopy
import logging

from keyboards.keyboards import create_inline_kb
from keyboards.answers_kb import create_answers_kb, QuestionsCallbackFactory

from lexicon.lexicon_ru import LEXICON_RU
from database.database import QUESTIONS_DB, USER_DB, POLL_CHOICE

# Инициализируем логгер
logger = logging.getLogger(__name__)

router = Router()


# Хэндлер на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    markup = create_inline_kb(2, 'choice', 'random', 'show_favorites', 'show_history')
    await message.answer(text=LEXICON_RU['/start'], reply_markup=markup)
    await message.delete()
    if message.from_user.id not in USER_DB:
        USER_DB[message.from_user.id] = deepcopy(POLL_CHOICE)
        logger.debug(f'Пользователь {message.from_user.id} добавлен в БД.')


@router.message(Command(commands='actions'))
async def process_actions_command(message: Message):
    markup = create_inline_kb(2, 'choice', 'random', 'show_favorites', 'show_history')
    await message.answer(text=LEXICON_RU['/actions'], reply_markup=markup)
    await message.delete()


# Хэндлер на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
    await message.delete()


@router.callback_query(F.data == 'choice')
async def process_yes_answer(callback: CallbackQuery):
    user = USER_DB[callback.from_user.id]
    id_q = len(user['answers'])
    markup = create_answers_kb(2, id_q)

    await callback.message.answer(text=QUESTIONS_DB[id_q], reply_markup=markup)
    await callback.message.delete()


@router.callback_query(F.data == 'random')
async def process_yes_answer(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['random'])
    await callback.message.delete()


@router.callback_query(F.data == 'show_favorites')
async def process_yes_answer(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['show_favorites'])
    await callback.message.delete()


@router.callback_query(F.data == 'show_history')
async def process_yes_answer(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['show_history'])
    await callback.message.delete()


@router.callback_query(QuestionsCallbackFactory.filter())
async def process_any_inline_button_press(callback: CallbackQuery, callback_data: QuestionsCallbackFactory):
    user = USER_DB[callback.from_user.id]
    user['answers'].append(callback_data.answer_id)
    id_q = len(user['answers']) if user['answers'] else 0

    if len(user['answers']) < len(QUESTIONS_DB):
        markup = create_answers_kb(2, id_q)

        await callback.message.answer(text=QUESTIONS_DB[id_q], reply_markup=markup)
    else:
        await callback.message.answer(text=f'Ваши ответы: {user['answers']}\n')
        await callback.message.answer(text='/actions')

        user['answers'].clear()

    await callback.message.delete()
