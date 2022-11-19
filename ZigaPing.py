#
#
# 
# 
# Name: ZigaPing
# Author: @AmErIcaNec_16
#meta developer: @AmErIcaNec_16
from .. import loader, utils
import time
import asyncio
import psutil

@loader.tds
class zing(loader.Module):
    """"""
    strings = {
    "name": "Zing"
    }

    @loader.command()
    async def zing(self, message):
        """показ характеристик вашего сервера"""
        cpu = psutil.cpu_percent()
        Ram = psutil.virtual_memory().percent
        ping_start = time.time()
        await message.edit(
        f"<b>проверка подожди...</b>"
        )
        ping_finish = time.time()

        await message.edit(
        f"<emoji document_id=5172533495162995360>⚡</emoji> <b>PING:</b> {round((ping_finish - ping_start)*1000, 2)} ms\n"
        f"<emoji document_id=5172861866887611077>💻</emoji> <b>CPU:</b> {cpu}%\n"
        f"<emoji document_id=5174693704799093859>🔞</emoji> <b>RAM:</b> {mem}%"
        )