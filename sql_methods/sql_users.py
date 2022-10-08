#################################################################################################################
#общие коды return для всех баз: 1 - все хорошо, 404 - чего-то нет, 606 - что-то уже есть 
#################################################################################################################
import sqlite3
import re
baseName = "comitet_db"
#################################################################################################################
#команда для запуска базы данных, где baseName - имя базы данных.
#################################################################################################################
def start_db():
	print('sql users base has been started')
	with sqlite3.connect(baseName) as sq:
		cursor = sq.cursor()
		table = """
		CREATE TABLE IF NOT EXISTS Users(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		login VARCHAR(30),
		keys VARCHAR(150)
	 	)
		"""
		cursor.executescript(table)
#################################################################################################################
#команда для создания пользователя.
#################################################################################################################
async def add_user(login):
	try:
		db = sqlite3.connect(baseName)
		cursor = db.cursor()
		cursor.execute("SELECT login FROM Users WHERE login = ?", [login])
		if cursor.fetchone() is not None:
			return 606
		else:
			cursor.execute("INSERT INTO Users(login) VALUES(?)", [login])
			db.commit()
			return 1
	finally:
		cursor.close()
		db.close()
#################################################################################################################
#команда для просмотра базы данных на сервере, пишет в консоль и не может быть использована в релизе!
#################################################################################################################
async def showUsers():
	db = sqlite3.connect(baseName)
	cursor = db.cursor()
	print("Users \n")
	cursor.execute("SELECT * FROM Users")
	usr = cursor.fetchall()
	print(usr) 
	print('\n')
	cursor.close()
	db.close()
#################################################################################################################
#команда для удаления пользователя по номеру в базе данных
#################################################################################################################
async def delete_user(id_):
	try:
		db = sqlite3.connect(baseName)
		cursor = db.cursor()
		cursor.execute("SELECT login FROM Users WHERE id = ?", [id_])
		if cursor.fetchone() is None:
			return 404
		else :
			cursor.execute("DELETE FROM Users WHERE id = ?", [id_])
			db.commit()
			return 1
	finally:
		cursor.close()
		db.close()
#################################################################################################################
#команда авторизации пользователя
#################################################################################################################
async def log_in(login):
	try:
		db = sqlite3.connect(baseName)
		cursor = db.cursor()
		cursor.execute("SELECT login FROM Users WHERE login = ?", [login])
		if cursor.fetchone() is None:
			return 404
		else:
			return 1
	finally:
		cursor.close()
		db.close()
#################################################################################################################
#команда регистраци пользователя на мероприятие по уникальному ключу мероприятия
#################################################################################################################
async def regKey(login,uniq):
	try:
		db = sqlite3.connect(baseName)
		cursor = db.cursor()
		cursor.execute("SELECT keys FROM Users WHERE login = ?",[login])
		tuple_keys = cursor.fetchone()
		newKeys = tuple_keys[0] + ',' + uniq
		cursor.execute("UPDATE Users SET keys = ? WHERE login = ?", [newKeys,login])
		db.commit()
	finally:
		cursor.close()
		db.close()
#################################################################################################################
#команда получения строки уникальных ключей пользователя через ',' 
#################################################################################################################
async def returnKeys(login):
	try:
		db = sqlite3.connect(baseName)
		cursor = db.cursor()
		cursor.execute("SELECT keys FROM Users WHERE login = ?",[login])
		tuple_keys = cursor.fetchone()
		return tuple_keys[0]
	finally:
		cursor.close()
		db.close()

b = '2022-11-11 11:11'
print(len(re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})",b)))