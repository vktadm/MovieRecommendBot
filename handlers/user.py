from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.keyboards import basic_actions_kb
from keyboards.create_inline_kb import create_answers_kb, QuestionsCallbackFactory

from lexicon.lexicon_ru import LEXICON_RU
from database.database import QUESTIONS_DB


router = Router()


# Хэндлер на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=basic_actions_kb)


# Хэндлер на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=basic_actions_kb)


@router.message(F.text == LEXICON_RU['choice'])
async def process_yes_answer(message: Message):
    markup = create_answers_kb(2, 1)
    await message.answer(text=QUESTIONS_DB[1], reply_markup=markup)


@router.message(F.text == LEXICON_RU['random'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['random'])


@router.message(F.text == LEXICON_RU['show_favorites'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['show_favorites'])


@router.message(F.text == LEXICON_RU['show_history'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['show_history'])


@router.callback_query(QuestionsCallbackFactory.filter())
async def process_any_inline_button_press(callback: CallbackQuery, callback_data: QuestionsCallbackFactory):
    await callback.message.answer(
        text=f'id вопроса: {callback_data.question_id}\n'
             f'id ответа: {callback_data.answer_id}\n'
    )
    await callback.answer()

