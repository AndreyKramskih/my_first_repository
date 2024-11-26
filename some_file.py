
#Из библиотеки aiogram импортируем классы Bot и Dispatcher
from aiogram import Bot, Dispatcher

#Из aiogram.filters импортируем класс Command,
# чтобы фильтровать апдейты по наличию в них команд,
# то есть сочетаний символов, начинающихся со знака "/".
from aiogram.filters import Command

#Из  aiogram.types импортируем класс Message. Апдейты этого типа мы будем ловить эхо-ботом.
from aiogram.types import Message

BOT_TOKEN='7656570135:AAHAU-5sKUFNc5UfgpBqEd4fxrKQWcQpoeU'

# Создаем объекты бота и диспетчера
# Инициализируем объекты бота и диспетчера. В качестве аргумента в Bot передаем BOT_TOKEN.
bot=Bot(token=BOT_TOKEN)
dp=Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )
# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

if __name__ =='__main__':
    dp.run_polling(bot)
