from datetime import date
import sqlite3


class Connexion():
	def __init__(self, connect, cursor):
		self.connect = connect
		self.cursor = cursor

	def create_usertable(self):
		self.connect.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, firstname TEXT, lastname TEXT, password TEXT, due_date DATE)')

	def create_actiontable(self):
		self.cursor.execute('CREATE TABLE IF NOT EXISTS actions(action_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, action TEXT, capital_entry TEXT, capital_rest TEXT, quantity INT, devise TEXT, start_date_ac DATE, end_date_ac DATE, due_date DATE)')

	def add_user(self, username, firstname, lastname, password, due_date):
		self.cursor.execute('INSERT INTO users(username, firstname, lastname, password, due_date) VALUES (?, ?, ?, ?, ?)',(username, firstname, lastname, password, due_date))
		self.connect.commit()
		return True

	def login(self, username, password):
		self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
		data = self.cursor.fetchall()
		return data

	def get_user_by_username(self, username):
		self.cursor.execute('SELECT * FROM users WHERE username="{}"'.format(username))
		data = self.cursor.fetchall()
		return data

	def add_action(self, user_id, action, capital_entry, capital_rest, quantity, devis, start_date_ac, end_date_ac, due_date):
		self.cursor.execute('INSERT INTO actions(user_id, action, capital_entry, capital_rest, quantity, devise, start_date_ac, end_date_ac, due_date) VALUES (?, ?, ?, ?, ?, ?, ?,?, ?)',(user_id, action, capital_entry, capital_rest, quantity, devis, start_date_ac, end_date_ac, due_date))
		self.connect.commit()

	def all_action_user(self, user_id):
		self.cursor.execute('SELECT * FROM actions WHERE user_id=?', (user_id))
		data = self.cursor.fetchall()
		return data

	def all_users(self):
		self.cursor.execute('SELECT * FROM users')
		data = self.cursor.fetchall()
		return data