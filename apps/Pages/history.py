import streamlit as st
from apps.Database.Connexion import Connexion as conn
import sqlite3
obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)

def app():
    st.title('historic of activities')

    st.subheader('fetch all action of user!')
    connect.create_actiontable()
    users = connect.all_users()
    st.write(users)
    lists = connect.all_action_user(1)
    st.write(lists) 