import streamlit as st
from apps.Database.Connexion import Connexion as conn
from datetime import date
import sqlite3

obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)
st.session_state.new_username = ''
# Define callback when text_input changed.
def on_changed():
    if "alias" not in st.session_state:
        st.session_state["alias"] = st.session_state.new_username

def app():
    st.set_page_config(page_title="Sign Up Page", page_icon=":bar_chart:") # , layout="wide"
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
            if 'register' not in st.session_state:
                st.session_state["register"] = new_username
            st.experimental_rerun()

