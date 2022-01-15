from Core.Page.BasePage import BasePage
import streamlit as st
import string
import random

class OrderPage(BasePage):
    session_state = None
    def __init__(self, session):
        super().__init__()
        self.session_state = session
        #self.order_page()
        
    def order_page(self):
        st.subheader('My Order Page')
        if st.button('Home', key=''.join(random.sample(string.ascii_lowercase,10))):
            self.getsession()
        
    def getsession(self):
        return self.session_state   
         
    def architecture(self):
        pass
