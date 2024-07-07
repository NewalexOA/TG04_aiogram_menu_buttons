from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Привет", callback_data="hello")],
        [InlineKeyboardButton(text="Пока", callback_data="goodbye")]
    ])
    return keyboard

def links_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://news.example.com")],
        [InlineKeyboardButton(text="Музыка", url="https://music.example.com")],
        [InlineKeyboardButton(text="Видео", url="https://video.example.com")]
    ])
    return keyboard

def dynamic_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ])
    return keyboard

def options_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
    ])
    return keyboard
