
#meta developer: @AmEriCaNec_16
#scope:hikka_only
import random
from .. import loader
from telethon.tl.types import Message
 

@loader.tds
class AnekdotiPhoto(loader.Module):
    """Memes 2022"""
    
    strings = {"name": "RandomPhotoAnekdot"}

    async def randomancmd(self, message: Message):
        """Send anekdot random """
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/aaakaramba/{random.randint(8, 2275)}">­</a>',
        )







