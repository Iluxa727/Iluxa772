
#meta developer: @AmEriCaNec_16
#scope:hikka_only
import random
from .. import loader
from telethon.tl.types import Message
 

@loader.tds
class MemesMod(loader.Module):
    """Memes 2022"""
    
    strings = {"name": "MemesPhoto"}

    async def memcmd(self, message: Message):
        """Send Memes photo"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/aaakaramba/{random.randint(8, 1077)}">­</a>',
        )






