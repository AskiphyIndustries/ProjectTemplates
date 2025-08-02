from aiogram import Bot, Dispatcher

import asyncio

import config.Config as config
import database.SQLIte3Connector as SQLIte3Connector
from handler import Commands, KeyboardCallback, Messages

settings = config.Config()

async def run_bot():
    bot = Bot(token=settings.BOT_TOKEN)

    dp = Dispatcher()

    dp.include_routers(
        Commands.router,
        KeyboardCallback.router,
        Messages.router
    )

    print("[Bot] Bot started!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

async def run_all():
    await asyncio.gather(run_bot(), SQLIte3Connector.create_tables())

if __name__ == '__main__':
    asyncio.run(run_all())