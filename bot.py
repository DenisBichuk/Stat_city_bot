from aiogram import executor
from loader import dp, bot
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands


if __name__ == '__main__':
    try:
        executor.start_polling(dp)
    except Exception():
        exit()
        executor.start_polling(dp)
