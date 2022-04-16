from aiogram import types
from database import database


async def send_welcome(message: types.Message):
    language = message.from_user.language_code
    user_id = message.from_user.id
    username = message.from_user.username
    if username is None:
        username = message.from_user.full_name
    database.add_user(username=username, user_id=user_id, language=language)
    await message.reply("Hello idiot. Are you ready to lose all your money?")


async def get_balance(message: types.Message):
    balance = database.get_balance(message.from_user.id)
    await message.reply(f"Ваш баланс: {balance} Р.")