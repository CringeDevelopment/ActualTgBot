import mysql.connector
from config import host, user, password, db_name, port

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

#ВНУТРЕННИЕ МЕРОПРИЯТИЯ
async def add_sub_inside(login):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM inside_subs WHERE login = %s",[login])
        if cursor.fetchone() is not None:
            return 606
        else:
            cursor.execute("INSERT INTO inside_subs(login) VALUES (%s)", [login])
            connection.commit()
            return 1
    finally:
        connection.close()


async def extract_inside_subs():
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT login FROM inside_subs")
        response = cursor.fetchall()
        if len(response) > 0:
            print (response)
        else:
            return 404
    finally:
        connection.close()

async def delete_inside_sub(login):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT login FROM inside_subs WHERE login = %s", [login])
        if cursor.fetchone() is None:
            return 404
        else:
            cursor.execute("DELETE FROM inside_subs WHERE login = %s", [login])
            connection.commit()
            return 1
    finally:
        connection.close()

#ВНЕШНИЕ МЕРОПРИЯТИЯ
async def add_sub_outside(login):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM outside_subs WHERE login = %s",[login])
        if cursor.fetchone() is not None:
            return 606
        else:
            cursor.execute("INSERT INTO outside_subs(login) VALUES (%s)", [login])
            connection.commit()
            return 1
    finally:
        connection.close()


async def extract_outside_subs():
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT login FROM outside_subs")
        response = cursor.fetchall()
        if len(response) > 0:
            print (response)
        else:
            return 404
    finally:
        connection.close()

async def delete_outside_sub(login):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT login FROM outside_subs WHERE login = %s", [login])
        if cursor.fetchone() is None:
            return 404
        else:
            cursor.execute("DELETE FROM outside_subs WHERE login = %s", [login])
            connection.commit()
            return 1
    finally:
        connection.close()