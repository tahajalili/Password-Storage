import sqlite3
from sqlite3 import *

SQL_CREATE_STATEMENT = '''CREATE TABLE password
             (id integer PRIMARY KEY NOT NULL,username text, password text, source text)'''
SQL_INSERT_STATEMENT = '''INSERT INTO password (username, password, source)VALUES(?,?,?)'''

DATABASE_PATH = '/PATH-TO-YOUR-DB/passDB.db'


def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
		print('Connection created.')
	except Error as e:
		return e

# def create_table(connection, sql_commands):
# 	c = connection.cursor()
# 	c.execute(sql_commands)
# 	print('=> Table created.')

def get_input():
	USERNAME = input('username: ')
	PASSWORD = input('password: ')
	SOURCE = input('source: ')
	return USERNAME,PASSWORD,SOURCE

def insert_date(connection,data):
	try:
		c = connection.cursor()
		c.execute(SQL_INSERT_STATEMENT, data)
		print('=> Data insertion done.')
	except Error as e:
		return e
	

def main():
	conn = create_connection(DATABASE_PATH)
	# create_table(conn, SQL_CREATE_STATEMENT)
	user_info = get_input()

	insert_date(conn, user_info)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()


