# from environs import Env
#
# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
#
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")
# ADMINS = env.list("ADMINS")
# IP = env.str("ip")  # Xosting ip manzili

import os

BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = list(os.environ.get("ADMINS"))
IP = str(os.environ.get("ip"))
PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))
