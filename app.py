import streamlit as st
from multiapp import MultiApp
from apps.Views import home, order, history, login, signup, logout # import your app modules here

st.set_page_config(page_title="Yahoo financial data visualization", page_icon=":bar_chart:") # , layout="wide"
app = MultiApp()

if 'auth_status' not in st.session_state:
    st.session_state['auth_status'] = False
    
# Add all your application here
app.add_app("Home", home.app)
app.add_app("Order", order.app)
app.add_app("Historique", history.app)

if 'auth_status' not in st.session_state or st.session_state['auth_status'] == False:
    app.add_app("Login", login.app)
    app.add_app("Signup", signup.app)
elif st.session_state['auth_status'] == True:    
    app.add_app("as "+ str(st.session_state.username), logout.app)

# The main app
app.run()


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}

            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

