from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

router_gratitude = Router()

def register_gratitude(dp):
    dp.include_router(router_gratitude)

class GratitudeFSM(StatesGroup):
    g1 = State()
    g2 = State()
    g3 = State()

@router_gratitude.message(Command("gratitude"))
async def gratitude(message: Message, state: FSMContext):
    await state.set_state(GratitudeFSM.g1)
    await message.answer("Напиши первую благодарность:")


@router_gratitude.message(GratitudeFSM.g1)
async def gratitude_1(msg: Message, state: FSMContext):
    await state.set_state(GratitudeFSM.g2)
    await msg.answer("Вторая:")


@router_gratitude.message(GratitudeFSM.g2)
async def gratitude_2(msg: Message, state: FSMContext):
    await state.set_state(GratitudeFSM.g3)
    await msg.answer("И третья:")


@router_gratitude.message(GratitudeFSM.g3)
async def gratitude_3(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("✨ Так держать!")