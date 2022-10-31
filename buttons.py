from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton

menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="📝 Buyurtma berish",callback_data="order")
	],
	[
	InlineKeyboardButton(text="⚡ Shoshilinch buyurtma",callback_data="rush_order")
	],
	[
	InlineKeyboardButton(text="💬 Bizning guruh",url="https://t.me/rosalie_tortlari")
	],
	]
)

menu2 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="🎂 Tort",callback_data="🎂 Tort")
	],
	[
	InlineKeyboardButton(text="🍰 Shirinlik",callback_data="🍰 Shirinlik")
	],
	[
	InlineKeyboardButton(text="🔙 Ortga",callback_data="orqa1")
	],
	]
)

menu3 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="📦 Pick up(самовывоз)",callback_data="pickup")
	],
	[
	InlineKeyboardButton(text="🚕 Yetkazib berish",callback_data="delivery")
	],
	[
	InlineKeyboardButton(text="🔙 Ortga",callback_data="orqa")
	],
	]
)

contact = ReplyKeyboardMarkup(
	keyboard = [
		[	
		KeyboardButton(text="📞 Raqam jo'natish",request_contact=True)
		]
	],
	resize_keyboard=True, one_time_keyboard=True
)

channel = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="📣 Bizning kanal",url="https://t.me/rosalie_tort")
	],
	]
)

menu5 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Reklama berish",callback_data="disp"),
    InlineKeyboardButton(text="Statistika",callback_data="stats")
	],
	]
)

reklamatasdiqlash= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Xa", callback_data="reklamaruxsat"),
            InlineKeyboardButton(text="❌ Yoq", callback_data="reklamaruxsatyuq")
        ],
    ],
)

tasdiqlash= InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="✅ Xa", callback_data="xa"),
			InlineKeyboardButton(text="❌ Yoq", callback_data="yuq")
		],
	],
)