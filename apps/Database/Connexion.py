from datetime import date
import sqlite3


class Connexion():
	def __init__(self, connect, cursor):
		self.connect = connect
		self.cursor = cursor

	def create_usertable(self):
		self.connect.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, firstname TEXT, lastname TEXT, capital REAL,rest_capital REAL, password TEXT, due_date DATE)')

	def create_actiontable(self):
		self.cursor.execute('CREATE TABLE IF NOT EXISTS action(user_id INT, action TEXT, capital_entry TEXT, capital_rest TEXT, quantity INT, devise TEXT, start_date_ac DATE, end_date_ac DATE, due_date DATE)')

	def add_user(self, username, firstname, lastname, capital, rest_capital, password, due_date):
		self.cursor.execute('INSERT INTO users(username, firstname, lastname, capital, rest_capital, password, due_date) VALUES (?, ?, ?, ?, ?, ?, ?)',(username, firstname, lastname, capital, rest_capital, password, due_date))
		self.connect.commit()

	def login(self, username, password):
		self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
		data = self.cursor.fetchall()
		return data

	def add_action(self, user_id, action, capital_entry, capital_rest, quantity, devis, start_date_ac, end_date_ac, due_date):
		self.cursor.execute('INSERT INTO users(user_id, action, capital_entry, capital_rest, quantity, devis, start_date_ac, end_date_ac, due_date) VALUES (?, ?, ?, ?, ?, ?, ?)',(user_id, action, capital_entry, capital_rest, quantity, devis, start_date_ac, end_date_ac, due_date))
		self.connect.commit()
