import streamlit as st
st.set_page_config(page_title="Log Out Page", page_icon=":bar_chart:") # , layout="wide"

def app():
    st.title('Logout Page')

    if st.button("Logout"):
        if 'auth' in st.session_state:
            st.session_state = {}  
            #st.experimental_rerun()          
        st.experimental_rerun() 
