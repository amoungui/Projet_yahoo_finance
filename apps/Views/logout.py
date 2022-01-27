import streamlit as st


def app():
    st.title('Logout Page')

    if st.button("Logout"):
        if 'auth' in st.session_state:
            st.session_state = {}  
            #st.experimental_rerun()          
        st.experimental_rerun() 
