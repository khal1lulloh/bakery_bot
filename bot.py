import logging
import config
from state import Delivery, Dispatch
from buttons import *
from db import Sql

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from typing import Union

# Configure logging
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token = config.Token, parse_mode='HTML')
dp = Dispatcher(bot, storage = storage)
db = Sql()
# list of admins
admin = ["""admin's id"""]

#the main part of the code
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	db.tablitsa_yaratish()
	user = message.from_user.username
	idi = message.from_user.id
	data1 = db.id_user(idi)
	if data1 is None:
		db.tablitsa_qushish(idi,user)
		await message.answer_photo(
			photo = open('image/img.jfif','rb'),
			caption = f'<b>Assalomu alaykum,</b> {message.from_user.first_name}!\n\n<b>"Rosalie tort"</b> shirinliklar olamining rasmiy botiga xush kelibsiz!\nBu yerda siz tortlar va shirinliklarga buyurtma berishingiz mumkin:',parse_mode='HTML',reply_markup=menu)
	else:
		await message.reply('<b>"Rosalie tort"</b> shirinliklar olamining rasmiy botiga xush kelibsiz!\n\nBu yerda siz tort va shirinliklarga buyurtma berishingiz mumkin:',reply_markup=menu)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
	await message.reply("<b>Xizmatlarimizdan foydalanish uchun /start ni bosing😊</b>")

@dp.callback_query_handler(text="rush_order")
async def rush_order(call: CallbackQuery):
	await call.message.answer("<b>Agar buyurtmangiz shoshilinch bo'lsa, iltimos shu nomerga murojaat qiling: +998881337444</b>")

@dp.callback_query_handler(text="order")
async def order(call: CallbackQuery):
    await call.message.answer("<b>Ikkita shartdan birini tanlang:</b>",reply_markup=menu3)
    await call.message.delete()

@dp.callback_query_handler(text="pickup")
async def pickup(call: CallbackQuery):
	idi = call.message.chat.id
	await call.message.answer("<b>Bizning manzil: Yakkasaroy tumani, Qushbegi mavzesi, 3\nMurojaat uchun raqam: +998881337444</b>")
	await bot.send_location(idi, latitude = '', longitude = '')

###################################### B A C K #######################################################
@dp.callback_query_handler(text="orqa")
async def orqa(call: CallbackQuery):
	await call.message.answer('<b>Xizmat turini tanlang:</b>',reply_markup=menu)
	await call.message.delete()


######## ordering part

@dp.callback_query_handler(text="delivery",states=None)
async def delivery(call: CallbackQuery):
    await call.message.answer("<b>Qaysi mahsulotga buyurtma bermoqchisiz?</b>",reply_markup=menu2)
    await call.message.delete()
    await Delivery.mahsulot.set()

@dp.callback_query_handler(state=Delivery.mahsulot)
async def tort(call: CallbackQuery, state:FSMContext):
	mahsulot = call.data
	if mahsulot == "orqa1":
		await call.message.answer("<b>O'zingizga qulay shartni tanlang:</b>",reply_markup=menu3)
		await call.message.delete()
		await state.finish()
		await state.reset_state()		
	else:
		await state.update_data(
			{'mahsulot':mahsulot}
			)
		await call.message.delete()
		await call.message.answer("<b>Buyurtma qoldirish uchun pastdigi tugmani bosib bizga telefon raqamingizni yuboring:👇</b>",reply_markup=contact)
		await Delivery.next()

@dp.message_handler(content_types='contact',state=Delivery.telefon)
async def get_contact(message: Message, state:FSMContext):
	telefon = message.contact.phone_number
	await state.update_data({"telefon_raqam": telefon})
	data2 = await state.get_data()
	global name,raqam
	name = data2.get("mahsulot")
	raqam = data2.get("telefon_raqam")
	d = "<b>ℹ️ Sizning buyurtmangiz!</b>\n\n"
	d += f"<b>Mahsulot turi: {name}\nTelefon raqamingiz: +{raqam}. Ma'lumotingiz tog'rimi?</b>"
	await message.answer(d,reply_markup=tasdiqlash)
	await state.finish()
	await state.reset_state()
	
@dp.callback_query_handler(text="xa")
async def uquv_markazlar_func(call: CallbackQuery):
	p = f"<b>Yangi buyurtma:\nIsmi: {call.message.chat.first_name}\nUsername: @{call.message.chat.username}\nTelefon raqam: +{raqam}\nTanlagan mahsuloti: {name}</b>"
	await bot.send_message(chat_id_of_the_adminstrator,p)
	await call.message.answer("<b>Siz bilan tez orada operatorimiz aloqaga chiqadi, vaqtdan unumli foydalanish uchun kanalimizga o'tishingiz va mahsulotlar bilan tanishishingiz mumkin</b>",reply_markup=channel)
	await call.message.delete()

@dp.callback_query_handler(text="yuq")
async def uquv_markazlar_func(call: CallbackQuery):
    await call.message.answer("<b>Buyurtmangiz bekor qilindi ✅</b>",reply_markup=menu)
    await call.message.delete()

###################################### A D M I N ############################################################

@dp.message_handler(text="/admin")
async def send_welcome(message: types.Message):
    idi = message.from_user.id
    if idi in admin:
        await message.answer("<b>Admin, xush kelibsiz!</b>",reply_markup=menu5)

@dp.callback_query_handler(text="disp")
async def uquv_markazlar_func19(call: CallbackQuery):
    await call.message.answer("Xabarni kiriting:")
    await Dispatch.xabar.set()

@dp.message_handler(state=Dispatch.xabar)
async def answer(message: types.Message, state: FSMContext):
    xab = message.text
    await state.update_data(
        {"xabar": xab}
    ) 
    date = await state.get_data()
    global habar
    habar = date.get("xabar")
    p = "Xabar tog'ri kiritilganmi?\n\n"
    p += f"<b>Xabar</b>: {habar}"

    await message.answer(p,parse_mode='HTML',reply_markup=reklamatasdiqlash)
    await state.finish()
    await state.reset_state()

@dp.callback_query_handler(text="reklamaruxsat")
async def uquv_markazlar(call: CallbackQuery):
    t = db.rec()
    for i in t:
        date2 = i[0]
        await bot.send_message(chat_id=date2,text=habar)
    await call.message.answer("<b>✅ Xabar yuborildi </b>",reply_markup=menu5)
    await call.message.delete()


@dp.callback_query_handler(text="reklamaruxsatyuq")
async def uquv_markazlar_func(call: CallbackQuery):
    await call.message.answer("<b> Xabar o'chirildi 🔥 </b>",reply_markup=menu5)
    await call.message.delete()

@dp.callback_query_handler(text="stats")
async def user(call: CallbackQuery):
    d = db.userlar()
    await call.message.answer(f"Foydalanuvchilar: {d} ta")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)