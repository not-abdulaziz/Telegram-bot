from aiogram import Bot,Dispatcher
import logging
from config import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())


