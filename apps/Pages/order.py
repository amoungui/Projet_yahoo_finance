import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import cufflinks as cf
import datetime


def app():
    st.title('Order ticker')

    start_date_order = st.date_input("Start date", datetime.date(2019, 1, 1))
    end_date_order = st.date_input("End date", datetime.date(2021, 1, 31))
    capital = st.text_input("Your entry capital")
    ticker_list_order = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
    tickerSymbol_order = st.selectbox('Stock ticker', ticker_list_order) # Select ticker symbol
    tickerData_order = yf.Ticker(tickerSymbol_order) # Get ticker data
    action = st.text_input("User Name", tickerData_order.info['open'])
    quantity = st.text_input("Your quantity")    
    if st.button("Add Action"):
        pass        
    
    