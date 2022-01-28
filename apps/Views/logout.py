import streamlit as st


def app():
    st.title('Logout Page')

    if st.button("Logout"):
        if 'auth_status' in st.session_state:
            st.session_state.auth_status = False        
        st.experimental_rerun() 
