from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="π Barcha Kategoriyalar"),
        ],
        # [
        #     # KeyboardButton(text="π Korzina"),
        #     KeyboardButton(text="βοΈ Sozlamalar"),
        # ],
        [
            KeyboardButton(text="π’ Biz bilan bog'lanish"),
        ],
    ],
    resize_keyboard=True,
)

#            KeyboardButton(text="πOrqaga"),
