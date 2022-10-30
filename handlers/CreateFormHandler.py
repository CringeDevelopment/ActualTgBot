from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from keyboards.reply_keyboards import AdminMainMenu
from sql_methods import sql_sublists
from keyboards.reply_keyboards import AdminMainMenu, AdministrationMenu, FormColumnMenu
#from keyboards import inline_keyboards
import re 
from source import admin_states
from source.admin_states import AdminState
from aiogram.dispatcher.filters import Text
global slovar

slovar = {
	'Завершить' : 'complete',
    'Логин' : 'log',
    'Имя' : 'name',
   'Описание' : 'description',
   'Фото' : 'photo',
   'Дата рождения' : 'BirthDate',
   'Факультет' : 'faculty',
   'Группа' : 'group_',
   'Курс' : 'course'
}


class FormSteps(StatesGroup):
	NewColumn = State()

async def WelcomeProcess(callback : types.CallbackQuery, state : FSMContext):
	a = callback.data.split('_')[2]
	await state.update_data(id_ = a) #BUGFIX
	await state.update_data(columns_arr = '')
	await callback.message.answer('Выберите параметры для будующей формы', reply_markup = FormColumnMenu)
	await FormSteps.NewColumn.set()

async def ColumnProcess(message : types.Message, state : FSMContext):

############### ПРОВЕРКА КОМАНДЫ ПО СЛОВАРЮ ####################################

	try:
		MessageResult = slovar[message.text]
	except:
		await message.answer('Пожалуйста, введите один из перечисленных параметров', reply_markup = FormColumnMenu)
		return

############### ЛОГИКА КНОПКИ ЗАВЕРШИТЬ ####################################

	if MessageResult == 'complete':
		data = await state.get_data()
		if len(data['columns_arr'].split('/')) < 1:
			await message.answer(f'{message.from_user.full_name} Пожалуйста, выберите параметры для формы!')
			return
		res = await sql_sublists.create_sublist(data['id_'], data['columns_arr'])
		if res == 1:
			await message.answer('Форма сохранена в базе данных', reply_markup = AdminMainMenu)
			await admin_states.SetAdmin()

############### НА СЛУЧАЙ ПОВТОРЯЮЩИХСЯ ПАРАМЕТРОВ ####################################

	else:
		data = await state.get_data()
		if MessageResult in data['columns_arr'].split('/'):
			await message.answer('Пожалуйста, введите новые параметры для формы')

############### ВЫВОД ВЫБРАННЫХ ПАРАМЕТРОВ И СОХРАНЕНИЕ ####################################

		else:
			if data['columns_arr'] != '': 
				new_data = data['columns_arr'] + '/' + MessageResult
			else : new_data = MessageResult
			await state.update_data(columns_arr = new_data)
			"""СОЗДАНИЕ ИНВЕРТИРОВАННОГО СЛОВАРЯ И ЕГО ЗАПИСЬ В ПЕРЕМЕННУЮ MSG
				ПРИВЕСТИ ПЕРЕМЕННЫЕ В ЧИТАЕМЫЙ ВИД И РАЗОБРАТЬСЯ В АЛГОРИТМЕ"""
			reversed_slovar = dict((v, k) for k, v in slovar.items())
			table_parameters = """Выбранные параметры формы:
"""
			for i in new_data.split('/'):
				table_parameters += f'|{reversed_slovar[i]}|'

			await message.answer(f"""{table_parameters}
Введите новые или нажмите 'завершить'""") #РАБОТАЕТ НЕКОРРЕКТНО

def register_CreateFormHandlers(dp : Dispatcher):
	dp.register_callback_query_handler(WelcomeProcess, Text(startswith="create_form_"), state = AdminState.admin)
	dp.register_message_handler(ColumnProcess, state=FormSteps.NewColumn)