import streamlit as st
from multiapp import MultiApp
from apps.Pages import home, order, history, login, signup # import your app modules here

st.set_page_config(page_title="Yahoo financial data visualization", page_icon=":bar_chart:") # , layout="wide"
app = MultiApp()


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Order", order.app)
app.add_app("Historique", history.app)
app.add_app("Login", login.app)
app.add_app("Signup", signup.app)
# The main app
app.run()


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
	            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

