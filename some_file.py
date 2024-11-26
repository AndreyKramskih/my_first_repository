
#Из библиотеки aiogram импортируем классы Bot и Dispatcher
from aiogram import Bot, Dispatcher

#Из aiogram.filters импортируем класс Command,
# чтобы фильтровать апдейты по наличию в них команд,
# то есть сочетаний символов, начинающихся со знака "/".
from aiogram.filters import Command

#Из  aiogram.types импортируем класс Message. Апдейты этого типа мы будем ловить эхо-ботом.
from aiogram.types import Message

# Чтобы наш эхо-бот мог срабатывать на отправку фото, добавим в его код некоторые импорты
from aiogram.types import ContentType
from aiogram import F

BOT_TOKEN='7656570135:AAHAU-5sKUFNc5UfgpBqEd4fxrKQWcQpoeU'

# Создаем объекты бота и диспетчера
# Инициализируем объекты бота и диспетчера. В качестве аргумента в Bot передаем BOT_TOKEN.
bot=Bot(token=BOT_TOKEN)
dp=Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )
# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)

# Обработчик для фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

# Обработчик для голосовых сообщений
async def send_voice_echo(message: Message):
    await message.answer_voice(message.voice.file_id)

#Обработчик видео
async def send_video_echo(message: Message):
    await message.answer_video(message.video.file_id)

# Обработчик видео сообщений
async def send_video_note_echo(message: Message):
    await message.answer_video_note(message.video_note.file_id)

# Обработчик стикеров
async def send_sticker_echo(message: Message):
    await message.answer_sticker(message.sticker.file_id)

# Обработчик для аудио файлов
async def send_audio_echo(message: Message):
    await message.answer_audio(message.audio.file_id)

# Обработчик файлов документов
async def send_file_echo(message: Message):
    await message.answer_document(message.document.file_id)

# Обработчик видео
async def send_video_echo(message: Message):
    await message.answer_video(message.video.file_id)


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_video_note_echo, F.video_note)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_file_echo, F.document)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_echo)

if __name__ =='__main__':
    dp.run_polling(bot)
