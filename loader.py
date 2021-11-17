from utils.db_api.database import dbworker
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datetime import *

from data import config

# время
now = datetime.now()
now = now.strftime("%Y-%m-%d")
now = datetime.strptime(now, '%Y-%m-%d')

if not config.TOKEN:
    exit("No token provided")

bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage = MemoryStorage())

# инициализируем базу данных
db = dbworker('db dumb1.db')
