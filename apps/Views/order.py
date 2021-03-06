import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import cufflinks as cf
import datetime
from apps.Database.Connexion import Connexion as conn
import sqlite3

obj_con = sqlite3.connect('data.my_db', check_same_thread=False)
cursor = obj_con.cursor()
connect = conn(obj_con, cursor)


def app():
    st.title('Order ticker')
    if st.session_state['auth_status'] == False:
        st.write('\n\n')
        st.info('Log in to get all Actions you want, Please go to login Page')
    else:
        user = connect.get_user_by_username(str(st.session_state.username))
        #st.write(user[0][0])
        start_date_order = st.date_input("Start date", datetime.date(2019, 1, 1))
        end_date_order = st.date_input("End date", datetime.date(2021, 1, 31))
        capital = st.text_input("Your entry capital")
        ticker_list_order = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
        tickerSymbol_order = st.selectbox('Stock ticker', ticker_list_order) # Select ticker symbol
        tickerData_order = yf.Ticker(tickerSymbol_order) # Get ticker data
        action = st.text_input("Your Action", tickerData_order.info['open'])
        quantity = st.text_input("Your quantity") 
        due_date = datetime.date.today()
        user_id = user[0][0]
        devis = tickerData_order.info['symbol'] 
        if st.button("Add Action"):
            connect.create_actiontable()
            capital_rest =  float(capital) - float(action)*float(quantity) 
            if capital_rest < 0:
                st.warning('Your Capital {} must not be less than action({})*quantity({})'.format(capital, action, quantity))
            else:
                result = connect.add_action(user_id, action, capital, capital_rest, quantity, devis, start_date_order, end_date_order, due_date)
                if result:
                    st.success("success added In as {}".format(tickerSymbol_order))
                    st.experimental_rerun()         
                st.success("Ticker success added In as {}, do you want ordered an other ticker?\n If not, go to historic Page to see the historic of your transactions".format(tickerSymbol_order))



