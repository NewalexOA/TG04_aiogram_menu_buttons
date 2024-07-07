from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router = Router()

class ExampleForm(StatesGroup):
    example_state = State()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! Я ваш новый бот. Как я могу помочь?")
    await state.set_state(ExampleForm.example_state)

@router.message(Command(commands=["help"]))
async def help(message: Message):
    help_text = (
        "Этот бот умеет выполнять следующие команды:\n"
        "/start - Запустить бота\n"
        "/help - Получить помощь по командам бота\n"
    )
    await message.answer(help_text)

@router.message(ExampleForm.example_state)
async def process_example_state(message: Message, state: FSMContext):
    await message.answer("Вы в примере состояния. Введите что-нибудь:")
    await state.clear()

def register_handlers(dp):
    dp.include_router(router)
