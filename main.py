import os
from pytube import YouTube
from aiogram import Bot, Dispatcher, executor, types
from filters import LinkCheck

from tg_token_api import API_TOKEN

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_help(msg: types.Message) -> None:
    await msg.answer("ПРивет! Я скину тебе видео из ютуба, чтобы ты смог сохранить.\n"
                     "Тебе нужно скинуть ссылку в формате ссылки или ид видео (например https://www.youtube.com/watch?v=dQw4w9WgXcQ\n"
                     "или dQw4w9WgXcQ) ")


@dp.message_handler(LinkCheck())
async def youtube_to_mp4(msg: types.Message) -> None:
    if not os.path.exists('static'):
        os.mkdir('static')
    video = YouTube(msg.text)
    quality = video.streams.get_highest_resolution()
    quality.download(output_path='static', filename=msg.text[:-11])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
