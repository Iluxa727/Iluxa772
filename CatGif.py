import random
from .. import loader
from telethon.tl.types import Message


@loader.tds
class GifCotik(loader.Module):
    """Тебе по названию не понятно?)"""
    
    strings = {"name": "gifCat"}

    async def catgfcmd(self, message: Message):
        """send random gif cat"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/simpampulki{random.randint}(https://t.me/simpampulki/1124,https://t.me/simpampulki/1559)">­</a>',
        )
