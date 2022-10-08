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


async def UserBackProcess(message : types.Message, state : FSMContext):
	await message.answer('return to main menu', reply_markup = UserMainMenu)


async def AdminBackProcess(message : types.Message, state : FSMContext):
	await message.answer('return to main menu', reply_markup = AdminMainMenu)
	await admin_states.SetAdmin()


def register_ServiceHandlers(dp : Dispatcher):
	dp.register_message_handler(UserBackProcess, commands = ['Назад'], state = AdminState.user or None)
	dp.register_message_handler(AdminBackProcess, commands = ['Назад'], state = [CreatingSteps,AdminState.admin])