from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

router_reflect = Router()

def register_reflect(dp):
    dp.include_router(router_reflect)

class ReflectFSM(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()

@router_reflect.message(Command("reflect"))
async def reflect(message: Message, state: FSMContext):
    await state.set_state(ReflectFSM.q1)
    await message.answer("Что сегодня получилось хорошо?")


@router_reflect.message(ReflectFSM.q1)
async def reflect_q1(msg: Message, state: FSMContext):
    await state.set_state(ReflectFSM.q2)
    await msg.answer("Что вызвало трудности?")


@router_reflect.message(ReflectFSM.q2)
async def reflect_q2(msg: Message, state: FSMContext):
    await state.set_state(ReflectFSM.q3)
    await msg.answer("Что сегодня узнал нового?")


@router_reflect.message(ReflectFSM.q3)
async def reflect_q3(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("💬 Жёстко!")