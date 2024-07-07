### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание

Это учебный проект бота для Telegram, созданный для демонстрации различных возможностей работы с инлайн-кнопками:

1. Показать простое меню с кнопками "Привет" и "Пока".
2. Показать инлайн-кнопки с URL-ссылками.
3. Динамическое изменение клавиатуры с кнопками "Показать больше", "Опция 1" и "Опция 2".

### Функциональность бота

#### 1. Простое меню с кнопками

Бот отображает меню с кнопками "Привет" и "Пока" при отправке команды `/start`. При нажатии на кнопку "Привет" бот отвечает "Привет, {имя пользователя}!", а при нажатии на кнопку "Пока" бот отвечает "До свидания, {имя пользователя}!".

#### 2. Кнопки с URL-ссылками

Бот отображает инлайн-кнопки с URL-ссылками на новости, музыку и видео при отправке команды `/links`.

#### 3. Динамическое изменение клавиатуры

Бот отображает инлайн-кнопку "Показать больше" при отправке команды `/dynamic`. При нажатии на эту кнопку бот заменяет её на две новые кнопки "Опция 1" и "Опция 2". При нажатии на любую из этих кнопок бот отправляет сообщение с текстом выбранной опции.

### Структура проекта

Проект состоит из следующих файлов и директорий:

- `main.py`: Главный файл для запуска бота. Инициализирует бота и диспетчер, устанавливает команды и запускает опрос обновлений.
- `config.py`: Файл конфигурации, содержащий токен бота.
- `handlers.py`: Содержит обработчики команд и сообщений бота.
- `keyboards.py`: Содержит функции для создания клавиатур с кнопками.
- `buttons.py`: Содержит функции для обработки нажатий кнопок.
- `requirements.txt`: Список зависимостей проекта.

---

## <a name="english"></a>Description in English

### Description

This is an educational project for a Telegram bot, created to demonstrate various capabilities of working with inline buttons:

1. Display a simple menu with "Hello" and "Goodbye" buttons.
2. Display inline buttons with URL links.
3. Dynamic keyboard changes with "Show More", "Option 1", and "Option 2" buttons.

### Bot Functionality

#### 1. Simple Menu with Buttons

The bot displays a menu with "Hello" and "Goodbye" buttons when the `/start` command is sent. When the "Hello" button is pressed, the bot replies "Hello, {user name}!", and when the "Goodbye" button is pressed, the bot replies "Goodbye, {user name}!".

#### 2. Buttons with URL Links

The bot displays inline buttons with URL links to news, music, and video when the `/links` command is sent.

#### 3. Dynamic Keyboard Changes

The bot displays an inline "Show More" button when the `/dynamic` command is sent. When this button is pressed, the bot replaces it with two new buttons "Option 1" and "Option 2". When either of these buttons is pressed, the bot sends a message with the text of the selected option.

### Project Structure

The project consists of the following files and directories:

- `main.py`: The main file for running the bot. It initializes the bot and dispatcher, sets commands, and starts polling for updates.
- `config.py`: Configuration file containing the bot token.
- `handlers.py`: Contains handlers for bot commands and messages.
- `keyboards.py`: Contains functions for creating keyboards with buttons.
- `buttons.py`: Contains functions for handling button presses.
- `requirements.txt`: List of project dependencies.
