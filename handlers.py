from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards import main_menu_keyboard, links_keyboard, dynamic_keyboard, options_keyboard
from buttons import handle_buttons, handle_dynamic_buttons

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Выберите действие:", reply_markup=main_menu_keyboard())

@router.message(Command(commands=["help"]))
async def help(message: Message):
    help_text = (
        "Этот бот умеет выполнять следующие команды:\n"
        "/start - Запустить бота\n"
        "/help - Получить помощь по командам бота\n"
        "/links - Показать ссылки на новости/музыку/видео\n"
        "/dynamic - Показать динамическое меню\n"
    )
    await message.answer(help_text)

@router.message(Command(commands=["links"]))
async def links(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=links_keyboard())

@router.message(Command(commands=["dynamic"]))
async def dynamic(message: Message):
    await message.answer("Показать больше опций:", reply_markup=dynamic_keyboard())

@router.callback_query()
async def callback_query_handler(callback_query: types.CallbackQuery):
    if callback_query.data in ["show_more", "option_1", "option_2"]:
        await handle_dynamic_buttons(callback_query)
    else:
        await handle_buttons(callback_query)

def register_handlers(dp):
    dp.include_router(router)
