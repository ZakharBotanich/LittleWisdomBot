from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import asyncio

router_focus = Router()

def register_focus(dp):
    dp.include_router(router_focus)

class FocusFSM(StatesGroup):
    goal = State()


@router_focus.message(Command("focus"))
async def focus(message: Message, state: FSMContext):
    await state.set_state(FocusFSM.goal)
    await message.answer("На чём хочешь сфокусироваться?")


@router_focus.message(FocusFSM.goal)
async def set_goal(msg: Message, state: FSMContext):
    kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="15 мин", callback_data="15"),
    InlineKeyboardButton(text="25 мин", callback_data="25"),
    InlineKeyboardButton(text="45 мин", callback_data="45")]
    ])
    await msg.answer("Выбери длительность:", reply_markup=kb)


@router_focus.callback_query(F.data.in_({"15", "25", "45"}))
async def start_timer(callback: CallbackQuery, state: FSMContext):
    duration = int(callback.data)

    await callback.message.answer(f"⏱ Таймер на {duration} минут запущен!")
    await callback.answer()

    await asyncio.sleep(duration * 60)

    await callback.message.answer("⏰ Время истекло!")

    await state.clear()