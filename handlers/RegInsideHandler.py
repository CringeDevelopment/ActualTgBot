from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.reply_keyboards import  UserMainMenu
from sql_methods import sql_admins, sql_users
from source import admin_states
from source.admin_states import AdminState

class InsideSteps(StatesGroup):
	Add = State()

async def WelcomeInsideProcess(message : types.Message, state : FSMContext):
	await message.answer('Hi, send me ur <u>NAME</u> and <u>PHOTO</u>')
	await InsideSteps.Add.set()

async def AddInsideProcess(message : types.Message, state : FSMContext):
	res = await sql_users.add_user(message.from_user.id, message.text, message.photo[0].file_id)
	if res == 606:
		await message.answer(f'{message.from_user.full_name} u already registred!', reply_markup = UserMainMenu)
		await admin_states.SetUser()
	else:
		await message.answer(f'Congradulations, {message.from_user.full_name}, u has been registred', reply_markup = UserMainMenu)
		await admin_states.SetUser()

def register_RegInsideHandlers(dp : Dispatcher):
	dp.register_message_handler(WelcomeInsideProcess, commands = ['reg'], state = '*')
	dp.register_message_handler(AddInsideProcess, content_types=['photo'],  state = InsideSteps.Add)