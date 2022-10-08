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
    'логин' : 'log',
    'имя' : 'name',
   'описание' : 'description',
   'фото' : 'photo',
   'дата рождения' : 'BirthDate',
   'факультет' : 'faculty',
   'группа' : 'group_',
   'курс' : 'course'
}

class FormSteps(StatesGroup):
	NewColumn = State()

async def WelcomeProcess(callback : types.CallbackQuery, state : FSMContext):
	await state.update_data(id_ = callback.data.split('_')[2][1]+callback.data.split('_')[2][2]) #ГЕНИАЛЬНОЕ РЕШЕНИЕ, НЕ КОСТЫЛЬ
	await state.update_data(columns_arr = '')
	await callback.message.answer('Welcome text, now u ll create form for event, u should only tap to keyboard', reply_markup = FormColumnMenu)
	await FormSteps.NewColumn.set()

async def ColumnProcess(message : types.Message, state : FSMContext):
	if message.text == 'ГОТОВО':
		data = await state.get_data()
		res = await sql_sublists.create_sublist(data['id_'], data['columns_arr'])
		if res == 1:
			await message.answer('nice', reply_markup = AdminMainMenu)
			await admin_states.SetAdmin()
	else:
		data = await state.get_data()
		if message.text in data['columns_arr'].split('/'):
			await message.answer('no no, only new buttons')
		else:
			new_data = data['columns_arr'] + '/'+message.text #КОСТЫЛЬ
			await state.update_data(columns_arr = new_data)
			await message.answer(f"""{data['columns_arr']} now, tap tap""") #РАБОТАЕТ НЕКОРРЕКТНО

def register_CreateFormHandlers(dp : Dispatcher):
	dp.register_callback_query_handler(WelcomeProcess, Text(startswith="create_form_"), state = AdminState.admin)

	dp.register_message_handler(ColumnProcess, state=FormSteps.NewColumn)