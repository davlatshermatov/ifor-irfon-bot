from aiogram import types
from loader import dp
from data.config import ADMINS


# only for admins
@dp.message_handler(content_types=types.ContentType.PHOTO, user_id=ADMINS)
async def get_file_id(message: types.Message):
    await message.reply("File ID: " + f"<code>{message.photo[-1].file_id}</code>")  # file_id

# # only for admins
# @dp.message_handler(content_types=types.ContentType.DOCUMENT, user_id=ADMINS)
# async def get_file_id(message: types.Message):
#     await message.reply("File ID: " + message.document.file_id)  # file_id
