from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру основных действий -------
button_choice = KeyboardButton(text=LEXICON_RU['choice'])
button_random = KeyboardButton(text=LEXICON_RU['random'])
button_show_favorites = KeyboardButton(text=LEXICON_RU['show_favorites'])
button_show_history = KeyboardButton(text=LEXICON_RU['show_history'])

# Инициализируем билдер для клавиатуры основных действий
basic_actions_kb_builder = ReplyKeyboardBuilder()
# Добавляем кнопки в билдер с аргументом width=2
basic_actions_kb_builder.row(button_choice, button_random,
                             button_show_favorites, button_show_history, width=2)
# Создаем клавиатуру с кнопками
basic_actions_kb: ReplyKeyboardMarkup = basic_actions_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# # Функция для генерации инлайн-клавиатур "на лету"
# def create_inline_kb(width: int,
#                      *args: str,
#                      last_btn: str | None = None,
#                      **kwargs: str) -> InlineKeyboardMarkup:
#     # Инициализируем билдер
#     kb_builder = InlineKeyboardBuilder()
#     # Инициализируем список для кнопок
#     buttons: list[InlineKeyboardButton] = []
#
#     # Заполняем список кнопками из аргументов args и kwargs
#     if args:
#         for button in args:
#             buttons.append(InlineKeyboardButton(
#                 text=LEXICON[button] if button in LEXICON else button,
#                 callback_data=button))
#     if kwargs:
#         for button, text in kwargs.items():
#             buttons.append(InlineKeyboardButton(
#                 text=text,
#                 callback_data=button))
#
#     # Распаковываем список с кнопками в билдер методом row c параметром width
#     kb_builder.row(*buttons, width=width)
#     # Добавляем в билдер последнюю кнопку, если она передана в функцию
#     if last_btn:
#         kb_builder.row(InlineKeyboardButton(
#             text=last_btn,
#             callback_data='last_btn'
#         ))
#
#     # Возвращаем объект инлайн-клавиатуры
#     return kb_builder.as_markup()
