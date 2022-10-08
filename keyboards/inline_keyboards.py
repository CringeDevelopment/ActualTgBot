from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BackButton = InlineKeyboardButton(text = "ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ", callback_data= "go_back")

TiosButton_1 = InlineKeyboardButton(text = "ИНФОРМАЦИЯ", callback_data= "tios_button_info")
TiosButton_2 = InlineKeyboardButton(text = "ДОСТИЖЕНИЯ", callback_data= "tios_button_achievments")
TiosButton_3 = InlineKeyboardButton(text = "КОНТАКТЫ", callback_data= "tios_button_contacts")
TiosMenu =  InlineKeyboardMarkup(row_width=1)
TiosMenu.insert(TiosButton_1).insert(TiosButton_2).insert(TiosButton_3).insert(BackButton)

BisButton_1 = InlineKeyboardButton(text = "ИНФОРМАЦИЯ", callback_data= "bis_button_info")
BisButton_2 = InlineKeyboardButton(text = "ДОСТИЖЕНИЯ", callback_data= "bis_button_achievments")
BisButton_3 = InlineKeyboardButton(text = "КОНТАКТЫ", callback_data= "bis_button_contacts")
BisMenu =  InlineKeyboardMarkup(row_width=1)
BisMenu.insert(BisButton_1).insert(BisButton_2).insert(BisButton_3).insert(BackButton)

SubButton_1 = InlineKeyboardButton(text = "ПОДПИСАТЬСЯ НА ВСЕ НОВОСТИ", callback_data = "sub_button_all")
SubButton_2 = InlineKeyboardButton(text = "ПОДПИСАТЬСЯ НА ВНУТРЕННИЕ НОВОСТИ", callback_data = "sub_button_inside")
SubButton_3 = InlineKeyboardButton(text = "ПОДПИСАТЬСЯ НА СТОРОННИЕ НОВОСТИ", callback_data = "sub_button_outside")
SubButton_4 = InlineKeyboardButton(text = "ОТПИСАТЬСЯ ОТ ВСЕХ НОВОСТЕЙ", callback_data = "sub_button_unsub")
SubMenu = InlineKeyboardMarkup(row_width = 1)
AdminSubMenu = InlineKeyboardMarkup(row_width=1)
AdminSubMenu.insert(SubButton_1).insert(SubButton_2).insert(SubButton_3).insert(SubButton_4).insert(BackButton)
SubMenu.insert(SubButton_3).insert(SubButton_4).insert(BackButton)

async def InlineFormMenu(id_): #ПЕРЕНЕСТИ В СЕРВИСНУЮ ПАПКУ
	BackButton = InlineKeyboardButton(text = "ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ", callback_data= "go_back")
	data = f'create_form_{id_}'
	CreateFormButton = InlineKeyboardButton(text = "СОЗДАТЬ ФОРМУ", callback_data= data)
	EventFormMenu = InlineKeyboardMarkup(row_width=1)
	EventFormMenu.insert(CreateFormButton).insert(BackButton)
	return EventFormMenu