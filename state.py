from aiogram.dispatcher.filters.state import StatesGroup, State

class Delivery(StatesGroup):
	mahsulot = State()
	telefon = State()

class Dispatch(StatesGroup):
	xabar = State()