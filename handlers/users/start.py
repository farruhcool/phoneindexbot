from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!, Введите часть телефонного номера '
                         f'как приведено на картинке, для получения информации о телефонной компании и местности')
    photo = InputFile(path_or_bytesio="photos/2.jpg")
    await message.answer_photo(photo=photo)
