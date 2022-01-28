import streamlit as st
from apps.Database.Connexion import Connexion as conn
import sqlite3

obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)


def app():
    st.title('Login')
    
    username = st.text_input("User Name")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        connect.create_usertable()
        result = connect.login(username, password)
        if len(result) != 0:
            if 'auth_status' not in st.session_state:
                st.session_state.auth_status = True
                st.session_state["username"] = username  
                st.success("Logged In as {}".format(username))
            else:
                st.session_state['auth_status'] = False             
            st.experimental_rerun() 
    