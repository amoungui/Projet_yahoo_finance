import streamlit as st
from Core.Page.HomePage import HomePage as homePage
from Core.Page.OrderPage import OrderPage as orderPage
import string
import random

st.set_page_config(page_title="Yahoo financial data visualization", page_icon=":bar_chart:") # , layout="wide"

def Homepage():
    st.session_state.runpage = main_page
    homepage = homePage(st.session_state.runpage)
    return homepage

def Orderpage():
	st.session_state.runpage = main_page
	orderpage = orderPage(st.session_state.runpage)
	return orderpage
 
def dashboard():
    st.subheader('Dashboard')
 
def main_page():
    btn1 = st.sidebar.button('Dashboard')
    btn2 = st.sidebar.button('Order Page')

    if btn1:
        st.session_state.runpage = Homepage
        home = Homepage()
        home.home_page()

    if btn2:
        st.session_state.runpage = Orderpage
        order = Orderpage()
        order.order_page()


    if 'runpage' not in st.session_state:
        st.session_state.runpage = main_page
        st.session_state.runpage()

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
	            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
if __name__ == '__main__':
    main_page()