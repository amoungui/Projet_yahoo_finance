import streamlit as st
from apps.Database.Connexion import Connexion as conn
from datetime import date
import sqlite3
obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)

def app():
    st.title('Signup')
    st.subheader("Create New Account")
    new_username = st.text_input("Username")
    new_firstname = st.text_input("firstname")
    new_lastname = st.text_input("lastname")
    new_password = st.text_input("Password", type='password')
    #new_capital = st.text_input("Initial Capital")  #new_capital,
    #new_captital_rest = 0 #  new_captital_rest,
    new_today_date = date.today()
    if st.button("Signup"):
        connect.create_usertable()
        if connect.add_user(new_username, new_firstname, new_lastname, new_password, new_today_date) == True:
            st.success("You have successfully created an account")
            st.info("Go to Login Menu to sign in")
            if 'register' not in st.session_state:
                st.session_state.register = {'username': new_username, 'firstname': new_firstname}
                st.experimental_rerun()
            st.experimental_rerun() 
            
        if connect.add_user(new_username, new_firstname, new_lastname, new_password, new_today_date) == False:
            st.warning('Please sure that you fill all the fields')

