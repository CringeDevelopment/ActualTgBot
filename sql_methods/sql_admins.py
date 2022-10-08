#################################################################################################################
#общие коды return для всех баз: 1 - все хорошо, 404 - чего-то нет, 606 - что-то уже есть 
#################################################################################################################
import mysql.connector
from config import host,user,password, db_name,port
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


#################################################################################################################
#добавить администратора, логин передается как число, пример : await add_admin(Ваш логин)
#################################################################################################################
async def add_admin(log):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM admin WHERE login = %s",[log])
        if cursor.fetchone() is not None:
            return 606
        else:
            cursor.execute("INSERT INTO admin(login) VALUES (%s)", [log])
            connection.commit()
            return 1
    finally:
        connection.close()




#################################################################################################################
#удалить администратора, id передается как число, пример : await delete_admin(Ваш id)
#################################################################################################################
async def delete_admin(id_):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id FROM admin WHERE id = %s", [id_])
        if cursor.fetchone() is None:
            return 404
        else:
            cursor.execute("DELETE FROM admin WHERE id = %s", [id_])
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
        cursor.execute("SELECT id FROM admin WHERE login = %s", [log])
        if cursor.fetchone() is None:
            return 404
        else:
            return 1
    finally:
        connection.close()
#################################################################################################################
#поставить выполняемый проект, проект передается как слово, лог как число ВНИМАНИЕ! ОБЩАЯ ДЛИНА СТРОКИ ПРОЕКТОВ НЕ ПРЕВЫШАЕТ 60 СИМВОЛОВ, пример : await add_project(Ваш логин ,Ваш prjct)
#################################################################################################################
async def add_project(log,prjct):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id FROM admin WHERE login = %s", [log])
        if cursor.fetchone() is None:
            return 404
        else:
            cursor.execute("UPDATE admin SET prjcts = %s WHERE login = %s", [prjct,log])
            connection.commit()
            return 1
    finally:
        connection.close()
