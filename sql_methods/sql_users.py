#################################################################################################################
#общие коды return для всех баз: 1 - все хорошо, 404 - чего-то нет, 606 - что-то уже есть 
#################################################################################################################
import mysql.connector
from config import host,user,password, db_name,port
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#################################################################################################################
#команда для запуска базы данных, стоит проверять наличие доступного подключения при запуске бота.
#################################################################################################################
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Exception as e:
        print("The error occurred", e)



async def CreateAcessMenu(log, isAdmin):
    AcessMenu = InlineKeyboardMarkup(row_width=1)
    if isAdmin == 404:
        Adata = f'make_admin_{log}'
        HighAcessButton = InlineKeyboardButton(text = "СДЕЛАТЬ АДМИНИСТРАТОРОМ", callback_data= Adata)
        AcessMenu.insert(HighAcessButton)
    Ddata = f'delete_{log}'
    DeleteButton = InlineKeyboardButton(text = "УДАЛИТЬ", callback_data= Ddata)
    AcessMenu.insert(DeleteButton)
    return AcessMenu


#################################################################################################################
#добавить администратора, логин передается как число, пример : await add_admin(Ваш логин)
#################################################################################################################
async def add_user(log, name, typ, photo):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM inside_subs WHERE login = %s",[log])
        if cursor.fetchone() is not None:
            return 606
        else:
            cursor.execute("INSERT INTO inside_subs(login, name, photo, type) VALUES (%s, %s, %s, %s)", [log, name, photo, typ])
            connection.commit()
            return 1
    finally:
        connection.close()




#################################################################################################################
#удалить администратора, id передается как число, пример : await delete_admin(Ваш id)
#################################################################################################################
async def delete_user(log):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT login FROM inside_subs WHERE login = %s", [log])
        if cursor.fetchone() is None:
            return 404
        else:
            cursor.execute("DELETE FROM inside_subs WHERE login = %s", [log])
            connection.commit()
            return 1
    finally:
        connection.close()

#################################################################################################################
#авторизация, логин передается как число, пример : await log_in(Ваш логин)
#################################################################################################################
async def log_in(log):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id FROM inside_subs WHERE login = %s", [log])
        if cursor.fetchone() is None:
            return 404
        else:
            return 1
    finally:
        connection.close()

async def show_users():
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM inside_subs")
        res = cursor.fetchall()
        if len(res)<1:
            return 404
        else:
            return res
    finally:
        connection.close()

async def show_user(log):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM inside_subs WHERE login = %s", [log])
        res = cursor.fetchone()
        if res is None:
            return 404
        else:
            return res
    finally:
        connection.close()