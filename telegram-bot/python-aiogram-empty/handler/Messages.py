from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config.Config as config
from fsm import FSM
from keyboard import KeyboardBuilder

settings = config.Config()

router = Router()

@router.message(F.text.lower() == 'пример', F.chat.type == 'private')
async def study(message: Message, state: FSMContext):
    await message.reply("Введите имя")
    await state.set_state(FSM.CarInfo.Label)
    return

@router.message(FSM.TestState.Name)
async def get_label(message: Message, state: FSMContext):
    await state.set_data({'name': message.text})

    await message.reply(f"Вас зовут: {message.text}")

