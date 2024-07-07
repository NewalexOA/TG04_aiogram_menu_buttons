from aiogram.types import CallbackQuery
from keyboards import options_keyboard

async def handle_buttons(callback_query: CallbackQuery):
    user_name = callback_query.from_user.first_name

    if callback_query.data == "hello":
        await callback_query.message.answer(f"Привет, {user_name}!")
    elif callback_query.data == "goodbye":
        await callback_query.message.answer(f"До свидания, {user_name}!")

    await callback_query.answer()

async def handle_dynamic_buttons(callback_query: CallbackQuery):
    if callback_query.data == "show_more":
        await callback_query.message.edit_reply_markup(reply_markup=options_keyboard())
    elif callback_query.data == "option_1":
        await callback_query.message.answer("Опция 1")
    elif callback_query.data == "option_2":
        await callback_query.message.answer("Опция 2")

    await callback_query.answer()
