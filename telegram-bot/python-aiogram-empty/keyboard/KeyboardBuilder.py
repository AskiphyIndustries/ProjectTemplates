from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

def reply_keyboard(buttons: list[str]) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    [keyboard.button(text=item) for item in buttons]
    keyboard.adjust(2)

    return keyboard.as_markup(resize_keyboard=True)

def inline_keyboard(buttons: list[InlineKeyboardButton]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    [keyboard.row(button) for button in buttons]

    keyboard.adjust(1)
    return keyboard.as_markup()