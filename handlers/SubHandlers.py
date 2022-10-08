from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from sql_methods import sql_lists
from keyboards.inline_keyboards import SubMenu


async def SubCallback(callback : types.CallbackQuery):
	result = callback.data.split('_')[2]
	if result == "all":
		InsideSubDataResult = await sql_lists.add_sub_inside(callback.from_user.id)
		OutsideSubDataResult = await sql_lists.add_sub_outside(callback.from_user.id)
		if InsideSubDataResult == 606 and OutsideSubDataResult == 606:
			await callback.message.answer('already sub all', reply_markup = types.ReplyKeyboardRemove())
		elif  InsideSubDataResult == 1 or OutsideSubDataResult == 1:
			await callback.message.answer('sub all', reply_markup = types.ReplyKeyboardRemove())
	elif result == "inside":
		InsideSubDataResult = await sql_lists.add_sub_inside(callback.from_user.id)
		if InsideSubDataResult == 1:
			await callback.answer('sub inside', show_alert=True )
		elif InsideSubDataResult == 606:
			await callback.answer('already sub', show_alert=True )
	elif result == "outside":
		OutsideSubDataResult = await sql_lists.add_sub_outside(callback.from_user.id)
		if OutsideSubDataResult == 1:
			await callback.answer('sub outside', show_alert=True )
		elif OutsideSubDataResult == 606:
			await callback.answer('already sub', show_alert=True )
	elif result == "unsub":
		InsideUnsubDataResult = await sql_lists.delete_sub_inside(callback.from_user.id)
		OutsideUnsubDataResult = await sql_lists.delete_sub_outside(callback.from_user.id)
		if InsideUnsubDataResult == 404 and OutsideUnsubDataResult == 404:
			await callback.message.answer('already unsub all', reply_markup = types.ReplyKeyboardRemove())
		elif  InsideUnsubDataResult == 1 or OutsideUnsubDataResult == 1:
			await callback.message.answer('sub all', reply_markup = types.ReplyKeyboardRemove())

def register_SubHandlers(dp : Dispatcher):
	dp.register_callback_query_handler(SubCallback, Text(startswith="sub_button_"))