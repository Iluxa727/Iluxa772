from .. import loader , utils 
from asyncio import sleep
import random
from telethon.tl.types import Message
#scope inline
 #Description new module 
 #scope: hikka_only
 #Commands .typ
 #.typ
 #meta developer: @AmErIcaNec_16 
@loader.tds 
class TypickMod(loader.Module):
	strings = {"name":"Typick"}
	
	async def typick(self,mesagge:Message) -> None:
		"Модуль для незнаю чого"
			...
		args = utils.get_args_raw(message)
		lol = ["Батя сказав сходи за пивом для його.", "Батя сказав ні.", "Батя сказав так",""]
		await message.delete()
		rand = random.choice(lol)
		fuckwar = await self.inline.form(message=utils.get_chat_id(message), text = "почекай пару секунд ...", reply_markup={"text": "Typick, "callback": devnull})
		await fuckwar.edit("📞 <b>Звонимо Баті...</b>")
		await sleep (1)
		war = ["1", "2", "3"]
		fuck = random.choice(war)
		ebal = ["Батя пішов пити пиво з Толіком","Батя курить","Батя дудлить пиво","Батя спалив як ти куриш тобі пізда","Мальчік шо ти робиш йди роби уроки","Батя сказав що він в твої роки вже з дівчатами гуляв а не в телевоні сидів"]
		hz = random.choice(ebal)
		if fuck  == war[0]:
			await fuckwar.edit(f":( <b>Батя не відповідає,перезвоніть потім</b>\n<b>можливо він {hz}<\b>")
			else:
				await fuckwar.edit("<b> Батя взяв трубку!!<\b>")
				await sleep (1)
				if args:
					await fuckwar.edit(f"<b>Відповідь Баті:<\b>\n- {rand}")
