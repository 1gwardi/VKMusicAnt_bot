import re

from aiogram import types
from aiogram.dispatcher.filters import Filter


class LinkCheck(Filter):
    key = 'is_link'
    pattern = re.compile(r'https://www.youtube.com/watch\?v=[\w]{11}')

    # [\w.-]+@[\w-]+\.(com|ru)  https://www.youtube.com/watch?v=dQw4w9WgXcQ
    async def check(self, msg: types.Message) -> bool:
        return self.pattern.match(msg.text)
