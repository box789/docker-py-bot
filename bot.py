import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# в ходе разработки токен будет в файле .env, а в продакшене - в переменной окружения
load_dotenv()

# Важный момент: мы НЕ пишем токен прямо в коде.
# Мы будем передавать его "снаружи", когда запустим контейнер.
# Это правило безопасности №1.
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я работаю внутри Docker-контейнера! 🐳")

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    if not TOKEN:
        print("Ошибка: Токен не найден!")
        return
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
