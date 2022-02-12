import asyncio
import threading

from aiogram import executor

from config import PORT
from data import server
from handlers.users import dp
from loader import bot, storage, botEventLoop
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)


async def on_shutdown(dispatcher):
    await bot.close()
    await storage.close()


def start_bot():
    asyncio.set_event_loop(botEventLoop)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown,
                           skip_updates=False)


def start_server():
    thread = threading.Thread(target=start_bot)
    thread.start()
    server.run(host='0.0.0.0', port=PORT, threaded=True, use_reloader=False)


if __name__ == "__main__":
    start_server()
