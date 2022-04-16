from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers.config import register_handlers

import logging
import os

from database import database
API_TOKEN = os.environ.get("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize FSM storage
memory_storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot, storage=memory_storage)


if __name__ == '__main__':
    database.init()
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)