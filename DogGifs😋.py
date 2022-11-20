#
#
#meta developer: @AmEriCaNec_16
#scope:Hikka_only
import random
from .. import loader
from telethon.tl.types import Message
 

@loader.tds
class DogGifs(loader.Module):
    """send random gifs dog"""
    
    strings = {"name": "DogGif"}

    async def dgcmd(self, message: Message):
        """send random dog gif"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/DailyDogGifs/{random.randint(2, 1449)}">­</a>',
        )





