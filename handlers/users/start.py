from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from utils.db_api import *
from keyboards.default import menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        await add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username
        )
    except Exception as e:
        print(e)

    await message.answer(
        f"Assalom Alekum,<b> {message.from_user.full_name}!</b>\nQuyidagi bo'limlardan birini tanlang 👇",
        reply_markup=menu)


@dp.message_handler(commands=['categories'])
async def get_category(message: types.Message):
    categories = await select_all_categories()
    await message.answer(f"category: {categories}")
