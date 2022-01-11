import streamlit as st
import pandas as pd
from datetime import date
import sqlite3

conn = sqlite3.connect('data.my_db')
c = conn.cursor()

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, firstname TEXT, lastname TEXT, capital REAL,rest_capital REAL, password TEXT, due_date DATE)')

def add_user(username, firstname, lastname, capital, rest_capital, password, due_date):
	c.execute('INSERT INTO users(username, firstname, lastname, capital, rest_capital, password, due_date) VALUES (?, ?, ?, ?, ?, ?, ?)',(username, firstname, lastname, capital, rest_capital, password, due_date))
	conn.commit()

def login(username, password):
	c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
	data = c.fetchall()
	return data

st.set_page_config(page_title="Yahoo financial data visualization", page_icon=":bar_chart:") # , layout="wide"

def main():
	""" Yahoo finance App """
	st.title("Yahoo finance App")
	menu = ["Home", "Login", "SignUp"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Home":
		st.subheader("Home")
	elif choice == "Login":
		st.subheader("Login Section")
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password", type='password')
		if st.sidebar.button("Login"):
			#if password == '12345':
			create_usertable()
			result = login(username, password)
			if result:
				st.success("Logged In as {}".format(username))
				task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")
				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("Profiles")
		else: 
			st.warning("Incorrect Username/Password")
	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_username = st.text_input("Username")
		new_firstname = st.text_input("firstname")
		new_lastname = st.text_input("lastname")
		new_password = st.text_input("Password", type='password')
		new_capital = st.text_input("Capital entry")
		new_captital_rest = 0
		new_today_date = date.today()
		if st.button("Signup"):
			create_usertable()
			add_user(new_username, new_firstname, new_lastname, new_capital, new_captital_rest, new_password, new_today_date)
			st.success("You have successfully created an account")
			st.info("Go to Login Menu to sign in")
	else:
		pass


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if __name__ == "__main__":
	main()