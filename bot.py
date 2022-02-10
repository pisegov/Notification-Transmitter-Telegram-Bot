import threading

from aiogram import executor

from data import server
from handlers.users import dp
from loader import bot, storage
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)


async def on_shutdown(dispatcher):
    await bot.close()
    await storage.close()


def startServer():
    server.run()


if __name__ == "__main__":
    threading.Thread(target=startServer).start()
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=False)
