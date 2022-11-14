from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import mysql.connector
from config import host,user,password, db_name,port

global slovar
slovar = {
    'log'  :  'INT',
    'name' : 'TEXT',
    'description' : 'TEXT',
    'photo' : 'TEXT',
    'BirthDate' : 'TEXT',
    'faculty' : 'TEXT',
    'group_' : 'TEXT',
    'course' : 'INT'
}




async def InlineRegMenu(isAdmin, isURL, id_, login_flag, log):
    RegMenu = InlineKeyboardMarkup(row_width = 1)
    if isAdmin != 404:
        DeleteData = f'EVENTdelete_{id_}'
        DeleteButton = InlineKeyboardButton(text = "УДАЛИТЬ МЕРОПРИЯТИЕ", callback_data=DeleteData)
        RegMenu.insert(DeleteButton)
    if login_flag == 1 and isURL == '0':
        UnSubData = f'unsub_event_{id_}_{log}'
        UnSubButton = InlineKeyboardButton(text = "ОТПИСАТЬСЯ", callback_data=  UnSubData)
        RegMenu.insert(UnSubButton)
        return RegMenu
    if login_flag == 404 and isURL == '0':
        SubData = f'sub_event_{id_}_{log}'
        SubButton = InlineKeyboardButton(text = "ПОДПИСАТЬСЯ", callback_data= SubData)
        RegMenu.insert(SubButton)
        return RegMenu
    if isURL != '0':
        UrlButton = InlineKeyboardButton(text = "ПРИНЯТЬ УЧАСТИЕ", url = isURL)
        RegMenu.insert(UrlButton)
        return RegMenu
    





async def InlineFormMenu(id_):
    BackButton = InlineKeyboardButton(text = "ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ", callback_data= "go_back")
    data = f'create_form_{id_}'
    CreateFormButton = InlineKeyboardButton(text = "СОЗДАТЬ ФОРМУ", callback_data= data)
    EventFormMenu = InlineKeyboardMarkup(row_width=1)
    EventFormMenu.insert(CreateFormButton).insert(BackButton)
    return EventFormMenu


async def try_sub(list_name, log):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        querry = f'SELECT log FROM sublist{list_name} WHERE log = %s'
        cursor.execute(querry, [log])
        if cursor.fetchone() is not None:
            return 1
        else:
            return 404
        #return 404
    finally:
        connection.close()

async def create_sublist(list_name, columns):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        columns.append('log')
        table_name = 'sublist' + str(list_name)
        create_querry = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' ('
        arr = columns
        for i in range (1, len(arr)): #КОСТЫЛЬ
            if i == len(arr) - 1:
                create_querry += arr[i] + ' ' + slovar[arr[i]] + ')' 
                break
            create_querry += arr[i] + ' ' + slovar[arr[i]] + ','
        cursor.execute(create_querry)
        connection.commit()
        return 1
    finally:
        connection.close()

async def add_sub(list_name, columns, content):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        test_querry = f'SELECT log FROM sublist{list_name} WHERE log = %s'
        cursor.execute(test_querry, [content[0]])
        if cursor.fetchone() is not None:
            return 606
        else:
            table_querry = f'INSERT INTO sublist{list_name}('
            columns_arr = columns.split('/')
            for i in range (0, len(columns_arr)):
                if i == len(columns_arr) - 1:
                    table_querry += columns_arr[i] + ' ' + ') VALUES (' + ('%s,'*(len(columns_arr)-1)) + '%s)'
                    break
                table_querry += columns_arr[i]  + ','
            cursor.execute(table_querry, content)
            connection.commit()
    finally:
        connection.close()

async def extract_subs(list_name):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        table_name = 'sublist' + str(list_name)
        extract_querry = 'SELECT * FROM ' + table_name
        cursor.execute(extract_querry)
        if cursor.fetchone() is None:
            return 404
        else:
            return cursor.fetchall()
    finally:
        connection.close()


async def delete_sub(list_name, log):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        table_name = 'sublist' + str(list_name)
        find_querry = 'SELECT * FROM ' + table_name + ' WHERE log = %s'
        cursor.execute(find_querry, [log])
        if cursor.fetchone() is None:
            return 404
        else:
            delete_querry = 'DELETE FROM ' + table_name + ' WHERE log = %s'
            cursor.execute(delete_querry, [log])
            connection.commit()
            return 1            
    finally:
        connection.close()


#async def delete_sublist(name):
#    connection = mysql.connector.connect(
#            host=host,
#            port = port,
#            user=user,
#            passwd=password,
#            database=db_name
#        )
#    cursor = connection.cursor()
#    try: