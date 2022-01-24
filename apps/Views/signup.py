import streamlit as st
from apps.Database.Connexion import Connexion as conn
from datetime import date
import sqlite3
obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)

# Define callback when text_input changed.
def on_changed():
    if "alias" not in st.session_state:
        st.session_state["alias"] = st.session_state.new_username

def app():
    st.title('Signup')
    st.subheader("Create New Account")
    new_username = st.text_input("Username", on_change=on_changed(), key='new_username')
    if connect.check_username_exist(str(st.session_state["alias"])):
        st.info('User '+ str(st.session_state["alias"]) + 'Already exist in database, please enter another username')    
    new_firstname = st.text_input("firstname")
    new_lastname = st.text_input("lastname")
    new_password = st.text_input("Password", type='password')
    #new_capital = st.text_input("Initial Capital")  #new_capital,
    #new_captital_rest = 0 #  new_captital_rest,
    new_today_date = date.today()
    if st.button("Signup"):
        connect.create_usertable()
        connect.add_user(new_username, new_firstname, new_lastname, new_password, new_today_date)
        result = connect.check_registration(new_username)
        if result:
            if 'register' not in st.session_state:
                st.session_state["register"] = new_username
            st.experimental_rerun()

