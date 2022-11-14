from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from keyboards.reply_keyboards import AdminMainMenu
from sql_methods import sql_sublists, sql_qq
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
   'Дата рождения' : 'birth',
   'Факультет' : 'faculty',
   'Группа' : 'group_',
   'Курс' : 'course',
   'id' : 'айди'
}

class FormSteps(StatesGroup):
	NewColumn = State()
	NewQuestion = State()

async def WelcomeProcess(callback : types.CallbackQuery, state : FSMContext):
	await state.reset_data()
	a = callback.data.split('_')[2]
	await state.update_data(id_ = a) #BUGFIX
	await state.update_data(columns_arr = ['id', ])
	await state.update_data(another_arr = [a, ])
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
		if len(data['columns_arr']) < 2:
			await message.answer(f'{message.from_user.full_name} Пожалуйста, выберите параметры для формы!')
			return
		if (len(data['columns_arr']) - len(data['another_arr'])) == 0:
			columns_result = await sql_sublists.create_sublist(data['id_'], data['columns_arr'])
			question_result = await sql_qq.add_qq(data['columns_arr'], data['another_arr'])
			if columns_result == 1 and question_result == 1 :
				await message.answer('Форма сохранена в базе данных', reply_markup = AdminMainMenu)
				await admin_states.SetAdmin()
############### НА СЛУЧАЙ ПОВТОРЯЮЩИХСЯ ПАРАМЕТРОВ ####################################

	else:
		data = await state.get_data()
		if MessageResult in data['columns_arr']:
			await message.answer('Пожалуйста, введите новые параметры для формы')

############### ВЫВОД ВЫБРАННЫХ ПАРАМЕТРОВ И СОХРАНЕНИЕ ####################################

		else: 
				
			buffer = data['columns_arr']
			buffer.append(MessageResult)
							
			await state.update_data(columns_arr = buffer)
			"""СОЗДАНИЕ ИНВЕРТИРОВАННОГО СЛОВАРЯ И ЕГО ЗАПИСЬ В ПЕРЕМЕННУЮ MSG
				ПРИВЕСТИ ПЕРЕМЕННЫЕ В ЧИТАЕМЫЙ ВИД И РАЗОБРАТЬСЯ В АЛГОРИТМЕ"""
			reversed_slovar = dict((v, k) for k, v in slovar.items())
			table_parameters = """Выбранные параметры формы: """			
			for i in data['columns_arr']:
				if i == 'id': #КОСТЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЛЬ
					pass
				else:
					table_parameters += f'|{reversed_slovar[i]}|'
			await message.answer(f"""{table_parameters} """) 
	
	if MessageResult != 'log' and MessageResult != 'complete':
		await message.answer(f'''Отправь мне вопрос, 
который бот задаст при заполнении поля ''', reply_markup = types.ReplyKeyboardRemove())
		await FormSteps.NewQuestion.set()

async def Question_Process(message : types.Message, state : FSMContext):
	data = await state.get_data()
	buffer_new = data['another_arr']
	buffer_new.append(message.text)
	await state.update_data(another_arr = buffer_new)
	await message.answer('''Вы добавили вопрос к колонке. Введите новые колонки или нажмите 'завершить' ''', reply_markup = FormColumnMenu)
	await FormSteps.NewColumn.set()
	
def register_CreateFormHandlers(dp : Dispatcher):
	dp.register_callback_query_handler(WelcomeProcess, Text(startswith="create_form_"), state = AdminState.admin)
	dp.register_message_handler(ColumnProcess, state=FormSteps.NewColumn)
	dp.register_message_handler(Question_Process, state=FormSteps.NewQuestion)