from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

BackReplyButton = KeyboardButton('/Назад')


RB1 = KeyboardButton('Соискатель')
RB2 = KeyboardButton('Разработчик')
RB3 = KeyboardButton('Дизайнер')
RB4 = KeyboardButton('Организатор')
RB5 = KeyboardButton('СММщик')
AspirantMenu = ReplyKeyboardMarkup(resize_keyboard = True).row(RB2, RB3).row(RB4, RB5).add(BackReplyButton)
RoleMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(RB1).row(RB2, RB3).row(RB4, RB5).add(BackReplyButton)


FormList = ['логин', 'имя', 'описание', 'фото', 'дата рождения', 'факультет', 'группа', 'курс',]


#FB - FormButton
CompleteButton = KeyboardButton('Завершить')
FB1 = KeyboardButton('Логин')
FB2 = KeyboardButton('Имя')
FB3 = KeyboardButton('Описание')
FB4 = KeyboardButton('Фото')
FB5 = KeyboardButton('Дата рождения')
FB6 = KeyboardButton('Факультет')
FB7 = KeyboardButton('Группа')
FB8 = KeyboardButton('Курс')
FormColumnMenu = ReplyKeyboardMarkup(resize_keyboard = True).row(FB1,FB2,FB3).row(FB4,FB5,FB6).row(FB7,FB8).add(CompleteButton).add(BackReplyButton)



MainButton_1 = KeyboardButton('/НОЦЫ_НИЛЫ')
MainButton_2 = KeyboardButton('/Контакты')
MainButton_3 = KeyboardButton('/О_комитете')
MainButton_4 = KeyboardButton('/Подписки')
MainButton_5 = KeyboardButton('/Администрация')
AdminMainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(MainButton_1, MainButton_2, MainButton_3).row(MainButton_4, MainButton_5)
UserMainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(MainButton_1, MainButton_2, MainButton_3).row(MainButton_4)


NotsNilButton_1 = KeyboardButton('/ТИОС')
NotsNilButton_2 = KeyboardButton('/БИС')
NotsNilButton_3 = KeyboardButton('/Прочее')
MenuNotsNil = ReplyKeyboardMarkup(resize_keyboard=True).row(NotsNilButton_1, NotsNilButton_2,
                                                            NotsNilButton_3).row(BackReplyButton)


AdministrationButton_1 = KeyboardButton('/Добавить_мероприятие')
#AdministrationButton_2 = KeyboardButton('/Удалить_мероприятие')
AdministrationButton_2 = KeyboardButton('/Управление_персоналом')
AdministrationMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(AdministrationButton_1, AdministrationButton_2).row(BackReplyButton)

EventTypeButton_1 = KeyboardButton('Внутреннее')
EventTypeButton_2 = KeyboardButton('Внешнее')

EventTypeMenu = ReplyKeyboardMarkup(resize_keyboard = True).row(EventTypeButton_1, EventTypeButton_2,BackReplyButton )
