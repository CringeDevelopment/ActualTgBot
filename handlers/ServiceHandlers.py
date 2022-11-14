from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.reply_keyboards import AdminMainMenu, EventTypeMenu, AdministrationMenu, UserMainMenu
from source import admin_states
#STATES
from source.admin_states import AdminState
from handlers.CreateEventHandler import CreatingSteps
from handlers.CreateFormHandler import FormSteps
from handlers.RegInsideHandler import InsideSteps


async def UserBackProcess(message : types.Message, state : FSMContext):
	await message.answer('Возвращаемся в главное меню', reply_markup = UserMainMenu)


async def AdminBackProcess(message : types.Message, state : FSMContext):
	await message.answer('Возвращаемся в главное меню', reply_markup = AdminMainMenu)
	await admin_states.SetAdmin()


def register_ServiceHandlers(dp : Dispatcher):
	dp.register_message_handler(UserBackProcess, commands = ['Назад'], state = [AdminState.user, InsideSteps])
	dp.register_message_handler(AdminBackProcess, commands = ['Назад'], state = [CreatingSteps,AdminState.admin, FormSteps ])