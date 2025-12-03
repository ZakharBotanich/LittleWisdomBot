from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

router_intent = Router()

def register_intent(dp):
    dp.include_router(router_intent)


class IntentFSM(StatesGroup):
    intent = State()
    support = State()

@router_intent.message(Command("intent"))
async def intent_cmd(message: Message, state: FSMContext):
    await state.set_state(IntentFSM.intent)
    await message.answer("Что хочешь сделать сегодня?")


@router_intent.message(IntentFSM.intent)
async def intent_step1(msg: Message, state: FSMContext):
    await state.set_state(IntentFSM.support)
    await msg.answer("Что поможет это сделать?")


@router_intent.message(IntentFSM.support)
async def intent_step2(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("🌅 Вперед!")