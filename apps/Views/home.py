import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import cufflinks as cf
import datetime

def app():
    st.title('Home Page')

    # App title
    st.markdown('''
        ## Search ticker information
    ''')
    st.write('---') 
    

    start_date = st.date_input("Start date", datetime.date(2019, 1, 1))
    end_date = st.date_input("End date", datetime.date(2021, 1, 31))

    # Retrieving tickers data
    ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
    tickerSymbol = st.selectbox('Stock ticker', ticker_list) # Select ticker symbol
    tickerData = yf.Ticker(tickerSymbol) # Get ticker data
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

    # Ticker information
    string_logo = '<img src=%s>' % tickerData.info['logo_url']
    st.markdown(string_logo, unsafe_allow_html=True)

    string_name = tickerData.info['longName']
    st.header('**%s**' % string_name)

    string_summary = tickerData.info['longBusinessSummary']
    st.info(string_summary)

    # Ticker data
    st.header('**Ticker data**')
    st.write(tickerDf)

    # Bollinger bands
    st.header('**Bollinger Bands**')
    qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
    qf.add_bollinger_bands()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)

    ####
    ### st.write(tickerData.info['financialCurrency'])