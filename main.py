'''
bot-downloader from yt to mp4 V1
'''

import os

from aiogram import Bot, Dispatcher, executor, types
from pytube import YouTube

from filters import LinkCheck
from tg_token_api import API_TOKEN

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

URI = 'https://www.youtube.com/watch?v='


# создаем шаблон для ссылки, чтобы проще взаимодействать с pytube

# старт-хендлер со инфой, что нужно писать в сообщении
@dp.message_handler(commands=['start', 'help'])
async def start_help(msg: types.Message) -> None:
    await msg.answer("ПРивет! Я скину тебе видео из ютуба, чтобы ты смог сохранить.\n"
                     "Тебе нужно скинуть ид видео (например из видоса https://www.youtube.com/watch?v=dQw4w9WgXcQ\n"
                     "ид - dQw4w9WgXcQ) ")


# мейн хендлер для обработки ссылки для скачивания видоса, сохранения в static и отправление юзеру
@dp.message_handler(LinkCheck())
async def youtube_to_mp4(msg: types.Message) -> None:
    await msg.answer('Преобразовываю...')
    os.chdir('static')
    link = msg.text
    yt = YouTube(URI + link)
    yt.streams.get_lowest_resolution().download(filename=f'{link}.mp4')
    while not os.path.exists(f'{link}.mp4'):
        if os.path.exists(f'{link}.mp4'):
            break
    await bot.send_video(msg.chat.id, open(f'{link}.mp4', 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
