import asyncio
from telegram import Bot

# Замените на ваш токен бота
TELEGRAM_BOT_TOKEN = '7118565111:AAFdA8D59Mw_lYYkB2fSZyprzsVkYEM0-f0'

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    # Получаем обновления
    updates = await bot.get_updates()

    for update in updates:
        print(update.message.chat.id)

# Запуск асинхронной функции
asyncio.run(main())