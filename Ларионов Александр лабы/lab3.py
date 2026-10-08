import asyncio

import aiohttp  # type: ignore
from aiogram import Bot, Dispatcher, types  # type: ignore

BOT_TOKEN = "8722254214:AAF-3fOuUu22SemuusqU5Uwx6Z9IDVAdSBI"
WEATHER_API_KEY = "ee3793b68bf0891a9a6e7a3c50a87aed"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def weather(message: types.Message):
    city = message.text.strip()
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric", "lang": "ru"}

    try:
        async with (
            aiohttp.ClientSession() as session,
            session.get(url, params=params, timeout=10) as response,
        ):
            if response.status != 200:
                await message.answer("Город не найден. Попробуй ещё раз.")
                return

            data = await response.json()

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        desc = data["weather"][0]["description"]

        text = (
            f"🌍 Город: {city}\n"
            f"🌡 Температура: {temp}°C\n"
            f"🤔 Ощущается как: {feels}°C\n"
            f"💨 Ветер: {wind} м/с\n"
            f"📝 Описание: {desc}"
        )
        await message.answer(text)

    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Ошибка при получении погоды. Попробуй позже.")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
