import streamlit as st


def app():
    st.title('Logout Page')

    if st.button("Logout"):
        if 'auth' in st.session_state:
            st.session_state['auth'] = {}
            st.session_state['username'] = {}        
        st.experimental_rerun() 
