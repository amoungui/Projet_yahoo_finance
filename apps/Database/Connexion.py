
class Connexion():
	def __init__(self, connect, cursor):
		self.connect = connect
		self.cursor = cursor

	def create_usertable(self):
		"""create user table into the database
		Args:
			None
		Returns:
			None
		"""        
		self.connect.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, firstname TEXT, lastname TEXT, password TEXT, due_date DATE)')

	def create_actiontable(self):
		"""create action table into the database
		Args:
			None
		Returns:
			None
		"""           
		self.cursor.execute('CREATE TABLE IF NOT EXISTS actions(action_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, action TEXT, capital_entry TEXT, capital_rest TEXT, quantity INT, devise TEXT, start_date_ac DATE, end_date_ac DATE, due_date DATE)')

	def add_user(self, username, firstname, lastname, password, due_date):
		"""insert user data into the user table
		Args:
			username(str), 
   			firstname(str), 
      		lastname(str), 
        	password(str), 
         	due_date(datetime)
		Returns:
			None
		"""            
		self.cursor.execute('INSERT INTO users(username, firstname, lastname, password, due_date) VALUES (?, ?, ?, ?, ?)',(username, firstname, lastname, password, due_date))
		self.connect.commit()

	def login(self, username, password):
		"""select user information into the user table
		Args:
			username (str), 
   			password (str)
		Returns:
			user informations
		"""          
		self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
		data = self.cursor.fetchall()
		return data

	def get_user_by_username(self, username):
		"""select user information by username
		Args:
			username (str)
		Returns:
			user (list) informations
		"""               
		self.cursor.execute('SELECT * FROM users WHERE username="{}"'.format(username))
		data = self.cursor.fetchall()
		return data

	def get_actions_by_id(self, id):
		"""select actions information by user id
		Args:
			id (str): user id
		Returns:
			actions (list) 
		"""                    
		self.cursor.execute('SELECT * FROM actions WHERE user_id="{}"'.format(id))
		data = self.cursor.fetchall()
		return data

	def add_action(self, user_id, action, capital_entry, capital_rest, quantity, devis, start_date_ac, end_date_ac, due_date):
		"""insert user data into the user table
		Args:
			user_id (int), 
   			action (str), 
      		capital_entry (str), 
        	capital_rest (str), 
         	quantity (int), 
          	devis (str), 
           	start_date_ac (datetime), 
            end_date_ac (datetime), 
            due_date (datetime)
		Returns:
			None
		"""
		self.cursor.execute('INSERT INTO actions(user_id, action, capital_entry, capital_rest, quantity, devise, start_date_ac, end_date_ac, due_date) VALUES (?, ?, ?, ?, ?, ?, ?,?, ?)',(user_id, action, capital_entry, capital_rest, quantity, devis, start_date_ac, end_date_ac, due_date))
		self.connect.commit()

	def all_action_user(self, user_id):
		"""select all actions information by user id
		Args:
			username (str)
		Returns:
			actions (tuple) 
		"""          
		self.cursor.execute('SELECT * FROM actions WHERE user_id=?', (user_id))
		data = self.cursor.fetchall()
		return data

	def all_users(self):
		"""select all users in the database
		Args:
			username (str)
		Returns:
			users (list) 
		"""               
		self.cursor.execute('SELECT * FROM users')
		data = self.cursor.fetchall()
		return data