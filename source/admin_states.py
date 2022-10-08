from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminState(StatesGroup):
	admin = State()
	user = State()

async def SetAdmin():
	await AdminState.admin.set()

async def SetUser():
	await AdminState.user.set()