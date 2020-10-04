from aiogram import types

import codes
from loader import dp


@dp.message_handler()
async def bot_code(message: types.Message):
    vxod = message.text
    if vxod in codes.kodlar:
        for n in codes.kodlar:
            if vxod == n:
                await message.reply(codes.kodlar[n])
    else:
        await message.reply("пока еще не существует в базе")