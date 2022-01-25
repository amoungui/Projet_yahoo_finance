import streamlit as st
from apps.Database.Connexion import Connexion as conn
import sqlite3
obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)
#str(st.session_state.username)

def app():
    if 'auth' not in st.session_state:
        st.title('historic of activities')

        st.subheader('fetch all action of user!')
                
        st.write('\n')
        st.info('Log in to view all your last transactions!')
    else:
        st.title('historic of activities')
        st.write('\n\n')
        st.subheader('user details')
        st.write('\n')        
        user = connect.get_user_by_username(str(st.session_state.username))
        st.write(user)
        st.write('\n\n')
        st.subheader('Your historic of transaction')
                