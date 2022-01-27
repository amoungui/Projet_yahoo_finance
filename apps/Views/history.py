import streamlit as st
import streamlit.components.v1 as components
from apps.Database.Connexion import Connexion as conn
import sqlite3

obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)
connect.create_actiontable()

def app():
    st.title('Historic of Transactions')
    if 'auth' not in st.session_state:
        st.write('\n')
        st.info('Log in to view all your last transactions!')
    else:
        st.write('\n')
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
            """.format(
                    user[0][1], 
                    user[0][2], 
                    user[0][3], 
                    user[0][4]
                )
            ,height=100,
        )                
        st.subheader('Your historic of transaction')
        user = connect.get_user_by_username(str(st.session_state.username))
        actions = connect.get_actions_by_id(user[0][0])
        #st.write(actions)
        if actions:
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
                        <th scope="col">alias</th>
                        <th scope="col">your action</th>
                        <th scope="col">capital entry</th>
                        <th scope="col">capital restant</th>
                        <th scope="col">quantity of action</th>
                        <th scope="col">devise of action</th>
                        <th scope="col">start date</th>
                        <th scope="col">end date</th>
                        <th scope="col">soumission date</th>
                    </tr>
                </thead>
                
                </table>
                """
                ,height=150,
            )           
            for i, action in enumerate(actions):
                components.html(
                    """
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>                
                        <table class="table">
                            <tbody>
                                <tr>
                                    <th scope="row"> > </th>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                </tr>
                            </tbody>
                        </table>
                    """.format(
                            str(user[0][1]), 
                            str(action[2]), 
                            str(action[3]), 
                            str(action[4]), 
                            str(action[5]), 
                            str(action[6]), 
                            str(action[7]), 
                            str(action[8]), 
                            str(action[9])
                        )
                    ,height=50,
                )                
        else:
            st.info("Currently, You haven't submitted any action, please go to order page to get action!")