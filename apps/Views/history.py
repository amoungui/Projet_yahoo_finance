import streamlit as st
from apps.Database.Connexion import Connexion as conn
import sqlite3
obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)
#str(st.session_state.username)

def app():
    st.title('historic of activities')

    st.subheader('fetch all action of user!')
    connect.create_actiontable()
    user = connect.check_username_exist(str(st.session_state.username))
    if user:
        pass
        #lists = connect.all_action_user(1)
    #if lists:
        #st.write(lists) 