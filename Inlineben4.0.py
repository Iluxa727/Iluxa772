__version__ = (3.0)
#и
from .. import loader, utils
from asyncio import sleep
import random
from telethon.tl.types import Message
#scope: inline
#Description версия 3.0
#scope: hikka_only
#Commands .beni
#.beni
#meta developer: @AmErIcaNec_16 
@loader.tds
class BenTalksMod(loader.Module):
	strings = {"name": "InlineBen"}
		
	async def ibencmd(self, message:Message) -> None:
		""" Поговори с  Бэном он хочет тебя Version 3.0"""
		async def devnull(*args):
			...
		args = utils.get_args_raw(message)
		lol = ["Yes.", "No.", "Ho ho ho...","Бэн сказал перезвони попоже"]
		await message.delete()
		rand = random.choice(lol)
		fuckwar = await self.inline.form(message=utils.get_chat_id(message), text = "подожди пару секунд...", reply_markup={"text": "BEN", "callback": devnull})
		await fuckwar.edit("📞 <b>Звоним Бэну...</b>")
		await sleep (1)
		war = ["1", "2", "3"]
		fuck = random.choice(war)
		ebal = ["хз" "спит", "в тренировке", "на отдыхе", "кинул тебя в чс", "набухался водки и лёг спать", "потерялся в мусорке", "шлепает твою дочку", "в мусарне", "ищет закладку", "вскрывает банку с шпротами", "кушает креветки", "сосет", "устанавливает хикку на хероку", "ждёт октето", "пишет модуль для группового секса", "пишет твоёй телке в PM", "курит кальян", "слушает мурчание твоей мамки в дискорде", "взламывает лавхост", "курит на балконе", "помогает юмаке копать огород", "упал в гроб при походе на кладбище", "раскидывает распальцовки c Bushido Zho", "курит alpha pvp", "ебет руку", "говнокодит", "играет в майнкрафт", "слушает мияги эндшпиль", "пиздит чужие коды с лицензией", "забыл поставить скобку и фиксит это пол дня","Ебет твою училку в рот","отключает тебе вайфай","Сосет","Сосёт Хуй Сашки"]
		hz = random.choice(ebal)
		if fuck == war[0]:
			await fuckwar.edit(f"📩 <b>Бэн не отвечает, перезвоните позже</b>\n<b>🤷‍♀️ Возможно он {hz}</b>")
		else:
			await fuckwar.edit("☎ <b>Внимание, Бэн принял вызов!</b>")
			await sleep (1)
			if args:	
				await fuckwar.edit(f"<b>Ваш вопрос:</b> <code>{args}</code>\n🧸 <b>Ответ Бэна:</b>\n- {rand}")
			else: await fuckwar.edit(f"🧸 <b>Ответ Бэна:</b>\n- {rand}")
