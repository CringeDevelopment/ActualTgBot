#################################################################################################################
#общие коды return для всех баз: 1 - все хорошо, 404 - чего-то нет, 606 - что-то уже есть, 808 - ошибка ввода 
#################################################################################################################
import mysql.connector
from config import host,user,password, db_name,port
from datetime import datetime
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
#команда для добавления мероприятия в базу данных : await add_event("Я - Мероприятие", "Я - Описание", "Я - дата в формате 2022/11/08 15:30:00", "Я - адрес фотографии")
#################################################################################################################
async def add_event(name,type_, description, dat, img, tags, web_source):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO events(name, locate, description, e_date, image, tags, web_source) VALUES (%s, %s, %s, %s, %s, %s, %s)", [name, type_, description, dat, img, tags, web_source]) 
        connection.commit()
        cursor.execute('SELECT MAX(id) from events')
        maxid = (cursor.fetchone()[0])
        #cursor.execute('SELECT id FROM events WHERE name = %s AND e_date = %s', [name, dat]) #ОЧЕНЬ НЕПРИЯТНЫЙ КОСТЫЛЬ
        return maxid
    finally:
        connection.close()
#################################################################################################################
#Команда которая извлечет из базы данных актуальные мероприятия которые еще не прошли до текущей даты : await extract_event() вернет данные в формате массива кортежей [('название','описание',datetime(дата),'адрес фотографии')]
#################################################################################################################
async def extract_events():
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        date_now = datetime.now()
        cursor.execute("SELECT id, name, description, e_date, image, web_source, locate FROM events WHERE e_date >= (%s)", [date_now])
        response = cursor.fetchall()
        if len(response) > 0:
            return response
        else:
            return 404
    finally:
        connection.close()

#################################################################################################################
#Команда, которая удаляет запись из таблицы по указанному id : await delete_event(1)
#################################################################################################################
async def delete_event(some_data):
    if (str(some_data)).isdigit() == False:    
        return 808
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT name FROM events WHERE id = (%s)", [some_data])
        if cursor.fetchone() is not None:
            cursor.execute("DELETE FROM events WHERE id = (%s)", [some_data])
            connection.commit()
            return 1
        else:
            return 404
    finally:
        connection.close()

async def clear_old():
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        date_now = datetime.now()
        cursor.execute("DELETE FROM events WHERE e_date < (%s)", [date_now])
    finally:
        connection.close()

async def extract_event_id(event_name):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT id FROM events WHERE name = (%s)', [event_name])
        if cursor.fetchone() is not None:
            return cursor.fetchone()
        else:
            return 404
    finally:
        connection.close()
