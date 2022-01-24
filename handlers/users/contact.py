from aiogram import types
from loader import dp


@dp.message_handler(text="📢 Biz bilan bog'lanish")
async def show_categories(message: types.Message):
    text = """
    Bizning kontaktlarimiz:
    📞 +998 90 511-10-00
    📞 +998 91 421-10-02
    📞 +998 90 511-00-00
    
    Telegram: @davlat_shermatov
    Instagram: <a href='https://instagram.com/ifor_irfon_korea?utm_medium=copy_link'>@ifor_irfon_korea</a>
    """
    await message.answer(text, parse_mode='html')
