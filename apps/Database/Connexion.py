from datetime import date
import sqlite3


class Connexion():
	def __init__(self, connect, cursor):
		self.connect = connect
		self.cursor = cursor

	def create_usertable(self):
	    self.connect.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, firstname TEXT, lastname TEXT, capital REAL,rest_capital REAL, password TEXT, due_date DATE)')

	def login(self, username, password):
	    self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
	    data = self.cursor.fetchall()
	    return data

	def create_usertable(self):
		self.cursor.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, firstname TEXT, lastname TEXT, capital REAL,rest_capital REAL, password TEXT, due_date DATE)')

	def add_user(self, username, firstname, lastname, capital, rest_capital, password, due_date):
		self.cursor.execute('INSERT INTO users(username, firstname, lastname, capital, rest_capital, password, due_date) VALUES (?, ?, ?, ?, ?, ?, ?)',(username, firstname, lastname, capital, rest_capital, password, due_date))
		self.connect.commit()


