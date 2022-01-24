from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Barcha Kategoriyalar"),
        ],
        # [
        #     # KeyboardButton(text="🗑 Korzina"),
        #     KeyboardButton(text="⚙️ Sozlamalar"),
        # ],
        [
            KeyboardButton(text="📢 Biz bilan bog'lanish"),
        ],
    ],
    resize_keyboard=True,
)

#            KeyboardButton(text="🔙Orqaga"),
