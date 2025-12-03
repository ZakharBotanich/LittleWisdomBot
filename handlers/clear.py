from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router_clear = Router()

def register_clear(dp):
    dp.include_router(router_clear)

@router_clear.message(Command("clear"))
async def clear_cmd(message: Message):
    await message.answer("Выгружай все, что хочешь сказать сюда.")
    @router_clear.message()
    async def process(msg: Message):
        await msg.answer("💭 Ухты!")
        router_clear.message.handlers.pop()