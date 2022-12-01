from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from keyboards.reply_keyboards import AdminMainMenu
from sql_methods import sql_sublists, sql_qq, sql_events
from keyboards.reply_keyboards import AdminMainMenu, AdministrationMenu, FormColumnMenu, FormNameColumnMenu
# from keyboards import inline_keyboards
import re
from source import admin_states
from source.admin_states import AdminState
from aiogram.dispatcher.filters import Text

global slovar

slovar = {
    'Завершить': 'complete',
    'Имя': 'name',
    'Описание': 'description',
    'Фото': 'photo',
    'Дата рождения': 'birth',
    'Факультет': 'faculty',
    'Группа': 'group',
    'Курс': 'course',
    'Номер телефона': 'phone',
    'ФИО капитана команды': 'capitan',
    'ФИО участника команды': 'teammates',
    'id': 'айди'
}


class FormSteps(StatesGroup):
    NewColumn = State()
    NewCountTeammates = State()
    NewName = State()
    NewQuestion = State()


async def WelcomeProcess(callback: types.CallbackQuery, state: FSMContext):
    await state.reset_data()
    a = callback.data.split('_')[2]
    await state.update_data(id_=a)  # BUGFIX
    await state.update_data(columns_arr=['id', ])
    await state.update_data(another_arr=[a, ])
    await state.update_data(amount_members='0')
    await callback.message.answer('Выберите параметры для будующей формы', reply_markup=FormColumnMenu)
    await FormSteps.NewColumn.set()

async def ColumnProcess(message: types.Message, state: FSMContext):
    ############### ПРОВЕРКА КОМАНДЫ ПО СЛОВАРЮ ####################################
    try:
        MessageResult = slovar[message.text]
    except:
        await message.answer('Пожалуйста, введите один из перечисленных параметров', reply_markup=FormColumnMenu)
        return



    match MessageResult:
        case 'name':
            data = await state.get_data()
            if ('capitan' and 'teammates') in data['columns_arr']:
                await message.answer('Пожалуйста, введите новые параметры для формы', reply_markup=FormColumnMenu)
                return
            elif ('capitan' or 'teammates') in data['columns_arr'] and data['amount_members'] != '1':
                await message.answer('''Выберите один из вариантов ниже''', reply_markup=FormNameColumnMenu)
                await FormSteps.NewName.set()
            elif (('capitan' or 'teammates') in data['columns_arr']) and data['amount_members'] == '1':
                await message.answer('Пожалуйста, введите новые параметры для формы', reply_markup=FormColumnMenu)
                return
            else:
                await message.answer('''Введите количество участников команды''',
                                     reply_markup=types.ReplyKeyboardRemove())
                await FormSteps.NewCountTeammates.set()

        case _:
            ############### ЛОГИКА КНОПКИ ЗАВЕРШИТЬ ####################################
            if MessageResult == 'complete':
                data = await state.get_data()
                if len(data['columns_arr']) < 2:
                    await message.answer(f'{message.from_user.full_name} Пожалуйста, выберите параметры для формы!')
                    return
                if (len(data['columns_arr']) - len(data['another_arr'])) == 0:
                    question_result = await sql_qq.add_qq(data['columns_arr'], data['another_arr'])

                    if 'teammates' in data['columns_arr']:
                        count_teammates = data['amount_members']
                        buffer_columns = data['columns_arr']
                        buffer_columns.remove('teammates')
                        team_columns = []
                        int_count = int(count_teammates)
                        for i in range(1, int_count):
                            team_columns.append('teammates')
                        buffer_columns.extend(team_columns)
                        await state.update_data(columns_arr=buffer_columns)

                    columns_result = await sql_sublists.create_sublist(data['id_'], data['columns_arr'])
                    columns_str = ''
                    count = 0
                    for i in data['columns_arr']:
                        if i != 'id':
                            match i:
                                case 'teammates':
                                    count += 1
                                    i += str(count)
                                    columns_str += '_' + i
                                case _:
                                    columns_str += '_' + i
                    await sql_events.add_event_clmns(data['id_'], columns_str)
                    if columns_result == 1 and question_result == 1:
                        await message.answer('Форма сохранена в базе данных', reply_markup=AdminMainMenu)
                        await admin_states.SetAdmin()
            ############### НА СЛУЧАЙ ПОВТОРЯЮЩИХСЯ ПАРАМЕТРОВ ####################################

            else:
                data = await state.get_data()
                if MessageResult in data['columns_arr']:
                    await message.answer('Пожалуйста, введите новые параметры для формы')
                    return

                ############### ВЫВОД ВЫБРАННЫХ ПАРАМЕТРОВ И СОХРАНЕНИЕ ####################################

                else:

                    buffer = data['columns_arr']
                    buffer.append(MessageResult)

                    await state.update_data(columns_arr=buffer)
                    """СОЗДАНИЕ ИНВЕРТИРОВАННОГО СЛОВАРЯ И ЕГО ЗАПИСЬ В ПЕРЕМЕННУЮ MSG
                        ПРИВЕСТИ ПЕРЕМЕННЫЕ В ЧИТАЕМЫЙ ВИД И РАЗОБРАТЬСЯ В АЛГОРИТМЕ"""
                    reversed_slovar = dict((v, k) for k, v in slovar.items())
                    table_parameters = """Выбранные параметры формы: """
                    for i in data['columns_arr']:
                        if i == 'id':  # КОСТЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЛЬ
                            pass
                        else:
                            table_parameters += f'|{reversed_slovar[i]}|'
                    await message.answer(f"""{table_parameters} """)

            if MessageResult != 'complete':
                await message.answer(f'''Отправь мне вопрос,  
    который бот задаст при заполнении поля ''', reply_markup=types.ReplyKeyboardRemove())
                await FormSteps.NewQuestion.set()


async def CountTeammates(message: types.Message, state: FSMContext):
    MessageResult = message.text
    try:
        int(MessageResult)
        if MessageResult <= '0':
            await message.answer('''Введите количество участников команды.
Пожалуйста, целым положительным числом.''', reply_markup=types.ReplyKeyboardRemove())
            await FormSteps.NewCountTeammates.set()
            return

        await state.update_data(amount_members=MessageResult)
        match MessageResult:
            case '1':
                data = await state.get_data()
                buffer = data['columns_arr']
                buffer.append('capitan')
                await state.update_data(columns_arr=buffer)
                """СОЗДАНИЕ ИНВЕРТИРОВАННОГО СЛОВАРЯ И ЕГО ЗАПИСЬ В ПЕРЕМЕННУЮ MSG
                    ПРИВЕСТИ ПЕРЕМЕННЫЕ В ЧИТАЕМЫЙ ВИД И РАЗОБРАТЬСЯ В АЛГОРИТМЕ"""
                reversed_slovar = dict((v, k) for k, v in slovar.items())
                table_parameters = """Выбранные параметры формы: """
                for i in data['columns_arr']:
                    if i == 'id':  # КОСТЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЛЬ
                        pass
                    else:
                        table_parameters += f'|{reversed_slovar[i]}|'
                await message.answer(f"""{table_parameters} """)

                await message.answer(f'''Отправь мне вопрос,  
                                           который бот задаст при заполнении поля ''',
                                     reply_markup=types.ReplyKeyboardRemove())
                await FormSteps.NewQuestion.set()

            case _:
                await message.answer('''Выберите один из вариантов ниже''', reply_markup=FormNameColumnMenu)
                await FormSteps.NewName.set()

    except:
        await message.answer('''Введите количество участников команды.
Пожалуйста, целым положительным числом.''', reply_markup=types.ReplyKeyboardRemove())
        await FormSteps.NewCountTeammates.set()
        return


async def NameBatton(message: types.Message, state: FSMContext):
    try:
        MessageResult = slovar[message.text]  # криво
    except:
        await message.answer('''Пожалуйста, введите один из перечисленных параметров''',
                             reply_markup=FormNameColumnMenu)
        return

    data = await state.get_data()
    if MessageResult in data['columns_arr']:
        await message.answer('''Пожалуйста, введите новые параметры для формы''',
                                     reply_markup=FormNameColumnMenu)
        return

    buffer = data['columns_arr']
    buffer.append(MessageResult)

    await state.update_data(columns_arr=buffer)
    """СОЗДАНИЕ ИНВЕРТИРОВАННОГО СЛОВАРЯ И ЕГО ЗАПИСЬ В ПЕРЕМЕННУЮ MSG
    ПРИВЕСТИ ПЕРЕМЕННЫЕ В ЧИТАЕМЫЙ ВИД И РАЗОБРАТЬСЯ В АЛГОРИТМЕ"""
    reversed_slovar = dict((v, k) for k, v in slovar.items())
    table_parameters = """Выбранные параметры формы: """
    for i in data['columns_arr']:
        if i == 'id':  # КОСТЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЛЬ
            pass
        else:
            table_parameters += f'|{reversed_slovar[i]}|'
    await message.answer(f"""{table_parameters} """)

    await message.answer(f'''Отправь мне вопрос,  
который бот задаст при заполнении поля ''', reply_markup=types.ReplyKeyboardRemove())
    await FormSteps.NewQuestion.set()


async def Question_Process(message: types.Message, state: FSMContext):
    data = await state.get_data()
    buffer_new = data['another_arr']
    buffer_new.append(message.text)
    await state.update_data(another_arr=buffer_new)
    await message.answer('''Вы добавили вопрос к колонке. Введите новые колонки или нажмите 'завершить' ''',
                         reply_markup=FormColumnMenu)
    await FormSteps.NewColumn.set()


def register_CreateFormHandlers(dp: Dispatcher):
    dp.register_callback_query_handler(WelcomeProcess, Text(startswith="create_form_"), state=AdminState.admin)
    dp.register_message_handler(ColumnProcess, state=FormSteps.NewColumn)
    dp.register_message_handler(CountTeammates, state=FormSteps.NewCountTeammates)
    dp.register_message_handler(NameBatton, state=FormSteps.NewName)
    dp.register_message_handler(Question_Process, state=FormSteps.NewQuestion)