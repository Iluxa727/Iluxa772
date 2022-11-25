
#meta developer: @AmEriCaNec_16
#scope:hikka_only
import random
from .. import loader
from telethon.tl.types import Message
 

@loader.tds
class ProgramSoft,script(loader.Module):
    """Soft program script"""
    
    strings = {"name": "RandomSoft"}

    async def sfcmd(self, message: Message):
        """Send random soft for you"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/+t0ynbAJwg1RhNGQy/{random.randint(8, 407)}">­</a>',
        )








