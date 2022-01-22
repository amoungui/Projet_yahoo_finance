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

    start_date_order = st.date_input("Start date", datetime.date(2019, 1, 1))
    end_date_order = st.date_input("End date", datetime.date(2021, 1, 31))
    capital = st.text_input("Your entry capital")
    ticker_list_order = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
    tickerSymbol_order = st.selectbox('Stock ticker', ticker_list_order) # Select ticker symbol
    tickerData_order = yf.Ticker(tickerSymbol_order) # Get ticker data
    action = st.text_input("Your Action", tickerData_order.info['open'])
    quantity = st.text_input("Your quantity") 
    due_date = datetime.date.today()
    user_id = 1
    devis = tickerData_order.info['financialCurrency'] 
    if st.button("Add Action"):
        connect.create_actiontable()
        capital_rest =  float(capital) - float(action)*float(quantity) 
        if capital_rest < 0:
            st.success("success added In as {}".format(tickerSymbol_order))
        else:
            result = connect.add_action(user_id, action, capital, capital_rest, quantity, devis, start_date_order, end_date_order, due_date)
            if result:
                st.success("success added In as {}".format(tickerSymbol_order))
                st.experimental_rerun()         
    
    
    st.subheader('fetch all action of user!')
    # connect.create_actiontable()
    # lists = connect.all_action_user(1)
    # st.write(lists)    