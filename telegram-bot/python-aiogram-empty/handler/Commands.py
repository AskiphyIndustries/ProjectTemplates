from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboard import KeyboardBuilder
from keyboard.KeyboardBuilder import inline_keyboard

router = Router()

@router.message(F.text.startswith('/start'))
async def start(message: Message):
    await message.reply("Здравствуйте.", reply_markup=KeyboardBuilder.reply_keyboard(["Пример"]))