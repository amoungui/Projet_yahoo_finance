import streamlit as st
from apps.Database.Connexion import Connexion as conn
from datetime import date
import sqlite3
import time

obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)
st.session_state.new_username = ''


def app():
    st.title('Signup')
    if 'register' in st.session_state:
        st.success('Welcome Ms/Mr {}, go to login page to log in! '.format(st.session_state["register"]))
        
    st.subheader("Create New Account")
    new_username = st.text_input("Username")
    new_firstname = st.text_input("firstname")
    new_lastname = st.text_input("lastname")
    new_password = st.text_input("Password", type='password')
    new_today_date = date.today()
    if st.button("Signup"):
        connect.create_usertable()
        connect.add_user(new_username, new_firstname, new_lastname, new_password, new_today_date)
        time.sleep(4)
        if connect.get_user_by_username(new_username):
            if 'register' not in st.session_state:
                st.session_state["register"] = new_username
            st.experimental_rerun()
        

