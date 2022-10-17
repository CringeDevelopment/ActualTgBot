from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.reply_keyboards import  UserMainMenu, AdminMainMenu
from sql_methods import sql_admins, sql_users
from source import admin_states
from source.admin_states import AdminState

global slovar
slovar = {
	404 : 'Сотрудник комитета',
	1 : 'Администратор ресурса',
	'aspirant1' : 'Поздравляем, ты прошел собеседование!',
	'aspirant0' : 'Кажется, ты не прошел собеседование('

}


async def ShowProcess(message : types.Message, state : FSMContext):
	UserList = await sql_users.show_users()
	UID = message.from_user.id
	if UserList == 404:
		await message.answer('NO INSIDE SUBS', reply_markup = AdminMainMenu)
		await admin_states.SetAdmin()
	else:
		for i in range(0, len(UserList)):
			a = await sql_admins.log_in(UserList[i][1])
			menu = await sql_users.CreateAcessMenu(UserList[i][1], a)
			await bot.send_photo(UID, UserList[i][3], f'{slovar[a]} {UserList[i][2]}, {UserList[i][4]}', reply_markup = menu)
		await bot.send_message(UID, f'{len(UserList)} peoples', reply_markup = AdminMainMenu)

async def AcessCallback(callback : types.CallbackQuery):
	log = callback.data.split('_')[2]
	result = await sql_admins.add_admin(log)
	if result == 606:
		await callback.answer('LOGIN ALREADY EXISTS', show_alert = True)
		await admin_states.SetAdmin()
	else:
		await callback.answer(f'{callback.from_user.full_name}, u create new admin', show_alert = True)
		await bot.send_message(log, f'Поздравляем, ты прошел собеседование!', reply_markup = AdminMainMenu)
		await admin_states.SetAdmin()

async def DeleteCallback(callback : types.CallbackQuery):
	log = callback.data.split('_')[1]
	await sql_users.delete_user(log)
	await sql_admins.delete_admin(log)
	await callback.message.delete()
	await bot.send_message(log, 'Кажется, ты не прошел собеседование(', reply_markup = UserMainMenu)
	await admin_states.SetAdmin()

def register_AcessHandlers(dp : Dispatcher):
	dp.register_message_handler(ShowProcess, commands = ['admin_acess'], state = AdminState.admin)

	dp.register_callback_query_handler(AcessCallback, Text(startswith="make_admin_"), state = AdminState.admin)
	dp.register_callback_query_handler(DeleteCallback, Text(startswith="delete_"), state = AdminState.admin)
