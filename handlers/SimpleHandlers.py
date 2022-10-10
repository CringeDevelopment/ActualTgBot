from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.reply_keyboards import AdminMainMenu, UserMainMenu, MenuNotsNil, AdministrationMenu
from keyboards.inline_keyboards import TiosMenu, SubMenu, AdminSubMenu, BisMenu
from sql_methods import sql_admins
from source import admin_states
from source.admin_states import AdminState
from handlers.CreateEventHandler import CreatingSteps


async def WelcomeProcess(message: types.Message):
	#global AdminResult
	AdminResult = await sql_admins.log_in(message.from_user.id)
	if AdminResult == 1:
		await admin_states.SetAdmin()
		await message.delete()
		await message.answer(f"{message.from_user.full_name} something welcome text, your status is Admin", reply_markup = AdminMainMenu)
	else:
		await admin_states.SetAdmin()
		await message.delete()
		await message.answer(f"{message.from_user.full_name} something welcome text, your status is User", reply_markup = UserMainMenu)

async def NotsNilProcess(message: types.Message):
	await message.delete()
	await message.answer("smthng nots nil info", reply_markup = MenuNotsNil)

async def AdminNotsNilProcess(message: types.Message):
	await message.delete()
	await message.answer("smthng nots nil info", reply_markup = MenuNotsNil)

async def ContactsProcess(message: types.Message):
	await message.delete()
	await message.answer("smthng contacts", reply_markup = UserMainMenu)

async def AdminContactsProcess(message: types.Message):
	await message.delete()
	await message.answer("smthng contacts", reply_markup = AdminMainMenu)

async def AboutProcess(message: types.Message):
	await message.delete()
	await message.answer("smthng about", reply_markup = UserMainMenu)

async def AdminAboutProcess(message: types.Message):
	await message.delete()
	await message.answer("smthng about", reply_markup = AdminMainMenu)

async def SubsProcess(message: types.Message):
	await message.delete()
	await message.answer("destroy keyboards", reply_markup = types.ReplyKeyboardRemove())
	await message.answer("smthng subs main", reply_markup = SubMenu)

async def AdminSubsProcess(message: types.Message):
	await message.delete()
	await message.answer("destroy keyboards", reply_markup = types.ReplyKeyboardRemove())
	await message.answer("smthng subs main", reply_markup = AdminSubMenu)

async def TiosProcess(message: types.Message):
	await message.delete()
	await message.answer("destroy keyboards", reply_markup = types.ReplyKeyboardRemove())
	await message.answer("smthng tios words", reply_markup = TiosMenu)

async def BisProcess(message: types.Message):
	await message.delete()
	await message.answer("destroy keyboards", reply_markup = types.ReplyKeyboardRemove())
	await message.answer("smthng tios words", reply_markup = BisMenu)

async def AdminTiosProcess(message: types.Message):
	await message.delete()
	await message.answer("destroy keyboards", reply_markup = types.ReplyKeyboardRemove())
	await message.answer("smthng tios words", reply_markup = TiosMenu)

async def AdminBisProcess(message: types.Message):
	await message.delete()
	await message.answer("destroy keyboards", reply_markup = types.ReplyKeyboardRemove())
	await message.answer("smthng tios words", reply_markup = BisMenu)

async def AdministrationProcess(message: types.Message):
	await message.delete()
	await message.answer("destroy keyboards", reply_markup = types.ReplyKeyboardRemove())
	await message.answer("for admins", reply_markup = AdministrationMenu)


async def UserBackCallback(callback : types.CallbackQuery):
	await callback.message.answer('return to main menu', reply_markup = UserMainMenu)

async def AdminBackCallback(callback : types.CallbackQuery):
	await callback.message.answer('return to main menu', reply_markup = AdminMainMenu)

async def TiosCallback(callback : types.CallbackQuery):
	result = callback.data.split('_')[2]
	if result == "info":
		await callback.message.answer('tios info')
	elif result == "achievments":
		await callback.message.answer('tios achievments')
	elif result == "contacts":
		await callback.message.answer('tios contacts')

async def BisCallback(callback : types.CallbackQuery):
	result = callback.data.split('_')[2]
	if result == "info":
		await callback.message.answer('bis info')
	elif result == "achievments":
		await callback.message.answer('bis achievments')
	elif result == "contacts":
		await callback.message.answer('bis contacts')

async def AdministrationCallback(callback : types.CallbackQuery):
	result = callback.data.split('_')[2]
	if result == 'addEvent':
		#добавление меро
		await callback.message.answer('add event')
	elif result == 'deleteEvent':
		#удаление меро
		await callback.message.answer('delete event')
	elif result == 'invite':
		#создание инвайт кода
		await callback.message.answer('create invite code')

def register_SimpleHandlers(dp : Dispatcher):
	dp.register_message_handler(WelcomeProcess, commands=['Start'], state = '*')
	dp.register_message_handler(NotsNilProcess, commands=['НОЦЫ_НИЛЫ'], state = AdminState.user)
	dp.register_message_handler(ContactsProcess, commands=['Контакты'], state = AdminState.user)
	dp.register_message_handler(AdminAboutProcess, commands=['О_комитете'], state=AdminState.admin)
	dp.register_message_handler(AdminNotsNilProcess, commands=['НОЦЫ_НИЛЫ'], state = AdminState.admin)
	dp.register_message_handler(AdminContactsProcess, commands=['Контакты'], state = AdminState.admin)
	dp.register_message_handler(AboutProcess, commands=['О_комитете'], state=AdminState.user)
	dp.register_message_handler(SubsProcess, commands=['Подписки'], state=AdminState.user)
	dp.register_message_handler(AdminSubsProcess, commands=['Подписки'], state= AdminState.admin)
	dp.register_message_handler(TiosProcess, commands=['ТИОС'], state=AdminState.user)
	dp.register_message_handler(BisProcess, commands=['БИС'], state=AdminState.user)
	dp.register_message_handler(AdminTiosProcess, commands=['ТИОС'], state=AdminState.admin)
	dp.register_message_handler(AdminBisProcess, commands=['БИС'], state=AdminState.admin)
	dp.register_message_handler(AdministrationProcess, commands=['Администрация'], state=AdminState.admin)

	dp.register_callback_query_handler(TiosCallback, Text(startswith="tios_button_"), state = '*')# BUGREPORT 
	dp.register_callback_query_handler(BisCallback, Text(startswith="bis_button_"), state = '*')# BUGREPORT
	dp.register_callback_query_handler(UserBackCallback, Text(startswith="go_back"), state = AdminState.user) #Заменить текст на лямбда функцию
	dp.register_callback_query_handler(AdminBackCallback, Text(startswith="go_back"), state = AdminState.admin)
	dp.register_callback_query_handler(AdministrationCallback, Text(startswith="administration_button_"), state=AdminState.admin)
