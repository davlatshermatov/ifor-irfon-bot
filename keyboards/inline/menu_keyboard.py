import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api import *

menu_cd = CallbackData("show_menu", "level", "category", "item_id")


def make_callback_data(level, category="0", item_id="0"):
    return menu_cd.new(
        level=level, category=category, item_id=item_id
    )


async def categories_keyboard():
    CURRENT_LEVEL = 0

    # Keyboard yaratamiz
    markup = InlineKeyboardMarkup(row_width=1)

    categories = await select_all_categories()
    for category in categories:
        # # Kategoriyaga tegishli mahsulotlar sonini topamiz
        # number_of_items = await db.count_products(category["category_code"])

        button_text = f"{category['name']}"

        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1, category=category['id']
        )

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return markup


# async def subcategories_keyboard(category_id):
#     CURRENT_LEVEL = 1
#
#     # Keyboard yaratamiz
#     markup = InlineKeyboardMarkup(row_width=1)
#
#     sub_categories = await select_all_subcategories(category_id)
#     for category in sub_categories:
#         button_text = f"{category['name']}"
#
#         callback_data = make_callback_data(
#             level=CURRENT_LEVEL + 1, category=category['id']
#         )
#
#         markup.insert(
#             InlineKeyboardButton(text=button_text, callback_data=callback_data)
#         )
#
#     markup.row(
#         InlineKeyboardButton(
#             text="⬅️Ortga", callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
#         )
#     )
#     return markup


# # Ostkategoriyaga tegishli mahsulotlar uchun keyboard yasaymiz
async def item_keyboard(product_id):
    CURRENT_LEVEL = 2

    markup = InlineKeyboardMarkup(row_width=1)
    button_text = f"🛒 Buyurtma berish"

    # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
    callback_data = make_callback_data(
        level=CURRENT_LEVEL + 1,
        item_id=product_id
    )
    markup.insert(
        InlineKeyboardButton(text=button_text, url="https://t.me/ifor_irfon_korea")
    )
    # markup.row(
    #     InlineKeyboardButton(
    #         text="⬅️Ortga",
    #         callback_data=make_callback_data(
    #             level=CURRENT_LEVEL - 1, category=category_id
    #         ),
    #     )
    # )
    return markup

# # Berilgan mahsulot uchun Xarid qilish va Ortga yozuvlarini chiqaruvchi tugma keyboard
# def item_keyboard(category, subcategory, item_id):
#     CURRENT_LEVEL = 3
#     markup = InlineKeyboardMarkup(row_width=1)
#     markup.row(
#         InlineKeyboardButton(
#             text=f"🛒 Xarid qilish", callback_data=buy_item.new(item_id=item_id)
#         )
#     )
#     markup.row(
#         InlineKeyboardButton(
#             text="⬅️Ortga",
#             callback_data=make_callback_data(
#                 level=CURRENT_LEVEL - 1, category=category, subcategory=subcategory
#             ),
#         )
#     )
#     return markup
