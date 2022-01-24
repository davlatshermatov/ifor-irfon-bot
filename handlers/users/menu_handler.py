import asyncio
from typing import Union

from aiogram import types
from aiogram.types import CallbackQuery, Message

from keyboards.inline.menu_keyboard import (
    menu_cd,
    categories_keyboard,
    # subcategories_keyboard,
    item_keyboard,
)
from loader import dp
from utils.db_api import *


@dp.message_handler(text="🛍 Barcha Kategoriyalar")
async def show_categories(message: types.Message):
    await list_categories(message)


# @dp.callback_query_handler(menu_cd.filter(level="1"))
# async def navigate_to_categories(call: CallbackQuery, callback_data: dict):
#     await list_subcategories(call, category=callback_data["category"])


@dp.callback_query_handler(menu_cd.filter(level="2"))
async def navigate_to_subcategories(call: CallbackQuery, callback_data: dict):
    await list_items(call, category=callback_data["category"])


# @dp.message_handler(text="🗑 Korzina")
# async def show_cart(message: types.Message):
#     # Foydalanuvchilarga o'zlarining korzinasini qaytaramiz
#     await message.answer("Korzina")


@dp.message_handler(text="⚙️ Sozlamalar")
async def show_settings(message: types.Message):
    # Foydalanuvchilarga sozlamalarni qaytaramiz
    await message.answer("Sozlamalar")


async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    markup = await categories_keyboard()

    if isinstance(message, Message):
        await message.answer("Bo'lim tanlang 👇", reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


# async def list_subcategories(callback: CallbackQuery, category, **kwargs):
#     markup = await subcategories_keyboard(category)
#     await callback.message.edit_reply_markup(markup)


async def list_items(callback: CallbackQuery, category, **kwargs):
    await callback.message.edit_text(text="Mahsulot tanlang")

    products = await get_products(category)
    for product in products:
        if product["image"]:
            await callback.message.answer_photo(
                photo=product["image"],
                caption=f"<b>{product['name']}</b>\n\n {product['description']}",
                reply_markup=await item_keyboard(product["id"]),
                parse_mode="HTML",
            )
            # sleep for 0.5 second
            await asyncio.sleep(0.5)

        else:
            await callback.message.answer(
                text=product["name"],
                reply_markup=await item_keyboard(product["id"]),
            )
            # sleep for 0.5 second
            await asyncio.sleep(0.5)


# Yuqoridagi barcha funksiyalar uchun yagona handler
@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """

    # Foydalanuvchi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    # Foydalanuvchi so'ragan Kategoriya
    category = callback_data.get("category")

    levels = {
        "0": list_categories,
        # "1": list_subcategories,
        "1": list_items,
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call, category=category
    )
