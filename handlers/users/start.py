from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!"
                         f"Добро пожаловать! Данный бот поможет вам выбрать тариф в складчину и расскажет о сервисе.")

