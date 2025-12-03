from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
router_сapture = Router()

def register_capture(dp):
    dp.include_router(router_сapture)

@router_сapture.message(Command("capture"))
async def capture(message: Message):
    await message.answer("Какие мысли и идеи хочешь сохранить?")
    @router_сapture.message()
    async def save(msg: Message):
        await msg.answer("📝 Отлично!")
        router_сapture.message.handlers.pop()