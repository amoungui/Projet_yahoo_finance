import streamlit as st
from Core.Page.HomePage import HomePage as homePage
from Core.Page.OrderPage import OrderPage as orderPage
import string
import random

def Homepage():
    st.session_state.runpage = main_page
    homepage = homePage(st.session_state.runpage)
    #homepage.home_page()
    return homepage

def Orderpage():
	st.session_state.runpage = main_page
	orderpage = orderPage(st.session_state.runpage)
	#orderpage.order_page()
	return orderpage
 
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

if __name__ == '__main__':
    main_page()