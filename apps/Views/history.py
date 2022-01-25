import streamlit as st
import streamlit.components.v1 as components
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
        # st.write(user)
        # bootstrap 4 collapse example
        components.html(
            """
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">username</th>
                    <th scope="col">First name</th>
                    <th scope="col">Last name</th>
                    <th scope="col">date entry</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="row"> > </th>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                </tr>
            </tbody>
            </table>
            """.format(user[0][1], user[0][2], user[0][3], user[0][4])
            ,height=600,
        )                
        st.write('\n\n')
        st.subheader('Your historic of transaction')
                