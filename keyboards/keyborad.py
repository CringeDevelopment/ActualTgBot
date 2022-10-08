from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton 
b1 = KeyboardButton('Команда1')
b2 = KeyboardButton('Команда2')
b4 = KeyboardButton('Команда3')
b5 = KeyboardButton('Команда4')
kb = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb.row(b2,b5).add(b1)


kb2 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb2.add(b1).add(b4)


kb3 = ReplyKeyboardMarkup(resize_keyboard = False, one_time_keyboard = True)
kb3.add(b2).row(b1,b4,b5)

inline_button_1 = InlineKeyboardButton(text = "Инлайн кнопка 1", callback_data= "inline_command_1")
inline_button_2 = InlineKeyboardButton(text = "Инлайн кнопка 2", url = 'https://vk.com/bonch.science')
inline_buttons = [InlineKeyboardButton(text = "Инлайн кнопка 3", callback_data= "inline_command_3"), InlineKeyboardButton(text = "Инлайн кнопка 4", callback_data= "inline_command_4")]
InlineMenu =  InlineKeyboardMarkup(row_width=1)
InlineMenu.add(inline_button_1).row(*inline_buttons).insert(inline_button_2)
