from aiogram import Router, F
from aiogram.filters import Command, StateFilter
import os
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove
from bot.keyboards.inline_kb.start_inline_kb import start_kb
from data.dbconnect import Request


router_commands = Router()

@router_commands.message(Command(commands=["start"]))
async def get_start(message: Message, request: Request):
    allowed_chat_ids = [int(chat_id) for chat_id in os.environ.get('allowed_chat_ids', '').split(',')]
    chat_id = message.chat.id
    if chat_id in allowed_chat_ids:
        await request.add_data(message.from_user.id, message.from_user.full_name)
        await message.answer(f"Привет{message.from_user.full_name}, для начала работы нажми начать."
                             f" Для ознакомления с инструкциями нажми инструкции.",
                             reply_markup=start_kb())
    else:
        await message.answer("У вас нет доступа к этому боту.")


@router_commands.message(Command(commands=["help"]))
async def get_help(message: Message):
    await message.answer("полная инструкция, для начала работы нажми начать.", reply_markup=start_kb())

@router_commands.message(StateFilter(None), Command("cancel"))
@router_commands.message(default_state, F.text.lower() == "отменить")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    # Стейт сбрасывать не нужно, удалим только данные
    await state.set_data({})
    await message.answer(
        text="Нечего отменять",
        reply_markup=start_kb()
    )


@router_commands.message(Command("cancel"))
@router_commands.message(F.text.lower() == "отменить")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )
