from telethon import TelegramClient, events
import asyncio

# Укажи свои данные API (получить можно на https://my.telegram.org/)
API_ID = 25109194  # Замени на свой API ID
API_HASH = "42d8365e2c8dfd49e978878c6afb992a"  # Замени на свой API Hash
USERNAME = "asteroalex"  # Юзернейм получателя

# Создание клиента сессии
client = TelegramClient("session", API_ID, API_HASH)

async def send_messages():
    while True:
        try:
            await client.send_message(USERNAME, "Привет!")
            print("Сообщение отправлено!")
        except Exception as e:
            print(f"Ошибка отправки: {e}")
        await asyncio.sleep(15)  # Ожидание 15 секунд

async def main():
    await client.start()
    print("Бот запущен!")
    await send_messages()

with client:
    client.loop.run_until_complete(main())
