from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from database.database import ANSWERS_DB


class QuestionsCallbackFactory(CallbackData, prefix='question', sep='-'):
    question_id: int
    answer_id: int


# ------- Создаем клавиатуру с ответами на вопрос -------
def create_answers_kb(width: int, q_id: int):
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками
    for key, value in ANSWERS_DB[q_id].items():
        buttons.append(InlineKeyboardButton(
            text=value,
            callback_data=QuestionsCallbackFactory(
                question_id=q_id,
                answer_id=key
            ).pack()
        ))
    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()
