from aiogram.types import Message

from loader import dp


@dp.message_handler()
async def echoAnswer(message: Message):
    await message.answer(message.text)
