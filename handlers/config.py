from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from handlers import common

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(common.get_balance,commands=['balance'])
    dp.register_message_handler(common.send_welcome, commands=["start", "help"])
