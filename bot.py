from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

from mytoken import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
    "Привет! Я LittleWisdomBot — помощник в технкиах осознанности. Вот что я умею:\n"
    "📝 /capture — захват мыслей\n"
    "💭 /clear — очистка разума\n"
    "🌅 /intent — намерение дня\n"
    "🧠 /reflect — вечерняя рефлексия \n"
    "✨ /gratitude — дневник благодарности\n"
    "⏱ /focus — фокус-сессия"
    )

from handlers.capture import register_capture
from handlers.clear import register_clear
from handlers.reflect import register_reflect
from handlers.intent import register_intent
from handlers.gratitude import register_gratitude
from handlers.focus import register_focus

register_capture(dp)
register_clear(dp)
register_reflect(dp)
register_intent(dp)
register_gratitude(dp)
register_focus(dp)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())