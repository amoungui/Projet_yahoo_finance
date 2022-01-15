from Core.Page.BasePage import BasePage
import streamlit as st
import string
import random


class HomePage(BasePage):
    session_state = None
    def __init__(self, session):
        super().__init__()
        self.session_state = session
        #self.home_page()
        
    def home_page(self):
        st.subheader('My Dashboard')
        if st.button('Home', key=''.join(random.sample(string.ascii_lowercase,10))):
            self.getsession()
        
    def getsession(self):
        return self.session_state
    
    def architecture(self):
        pass
