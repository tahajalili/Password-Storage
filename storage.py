#!/usr/bin/python3
__author__ = "Taha Jalili"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "tahajalili@gmail.com"

import sys
import sqlite3
from sqlite3 import *
import inquirer

SQL_CREATE_STATEMENT = '''CREATE TABLE password
             (id integer PRIMARY KEY NOT NULL,username text, password text, source text)'''
SQL_INSERT_STATEMENT = '''INSERT INTO password (username, password, source)VALUES(?,?,?)'''

DATABASE_PATH = '/home/taha/lessons/projects/passStorage/passDB.db'


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

def show_info(connection):
	c = connection.cursor()
	info = c.execute('SELECT * FROM password ORDER BY id')
	print('YOUR PASSWORDS'.center(45,'-'))
	print('(id, username, password, source)')
	for row in info:
		print(row,'')
	print('\n')

def ask_again():
	user_choice = input("Wish to continue? Y/N ")
	if user_choice == 'y' or user_choice == 'Y':
		main()
	elif user_choice == 'n' or user_choice == 'N':
		print("==> BYE <==")
		sys.exit(0)

def main():
	conn = create_connection(DATABASE_PATH)
	# create_table(conn, SQL_CREATE_STATEMENT)
	
	questions = [
		inquirer.List(
				'job',
				message = 'What should I do?',
				choices=['Add data','Show saved data.']
			),
		]
	answers = inquirer.prompt(questions)
	
	if answers['job'] == 'Add data':
		user_info = get_input()
		insert_date(conn, user_info)
	elif answers['job'] == 'Show saved data.':
		show_info(conn)
	
	ask_again()	
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()


