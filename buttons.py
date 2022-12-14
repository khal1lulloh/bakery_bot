from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton

menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="π Buyurtma berish",callback_data="order")
	],
	[
	InlineKeyboardButton(text="β‘ Shoshilinch buyurtma",callback_data="rush_order")
	],
	[
	InlineKeyboardButton(text="π¬ Bizning guruh",url="https://t.me/rosalie_tortlari")
	],
	]
)

menu2 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="π Tort",callback_data="π Tort")
	],
	[
	InlineKeyboardButton(text="π° Shirinlik",callback_data="π° Shirinlik")
	],
	[
	InlineKeyboardButton(text="π Ortga",callback_data="orqa1")
	],
	]
)

menu3 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="π¦ Pick up(ΡΠ°ΠΌΠΎΠ²ΡΠ²ΠΎΠ·)",callback_data="pickup")
	],
	[
	InlineKeyboardButton(text="π Yetkazib berish",callback_data="delivery")
	],
	[
	InlineKeyboardButton(text="π Ortga",callback_data="orqa")
	],
	]
)

contact = ReplyKeyboardMarkup(
	keyboard = [
		[	
		KeyboardButton(text="π Raqam jo'natish",request_contact=True)
		]
	],
	resize_keyboard=True, one_time_keyboard=True
)

channel = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="π£ Bizning kanal",url="https://t.me/rosalie_tort")
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
            InlineKeyboardButton(text="β Xa", callback_data="reklamaruxsat"),
            InlineKeyboardButton(text="β Yoq", callback_data="reklamaruxsatyuq")
        ],
    ],
)

tasdiqlash= InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="β Xa", callback_data="xa"),
			InlineKeyboardButton(text="β Yoq", callback_data="yuq")
		],
	],
)