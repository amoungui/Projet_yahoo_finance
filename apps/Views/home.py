import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import cufflinks as cf
import datetime

#################################################################
def stock_data(ticker_df):
    st.header('Rendement')
    # use numerical integer index instead of date    
    #ticker_df = ticker_df.reset_index()
    #ticker_df.rename(columns={'Adj Close': 'Adj_Close'}, inplace=True)

    rendement=ticker_df['Adj Close'].pct_change()
    #rendement=(1+rendement).cumprod()
    rendement[0]=1
    #print(rendement) 

    fig, ax =plt.subplots(figsize=(12,6)) # 6
    plt.plot(ticker_df.index, rendement, linestyle='dashed', marker='o', color ='b', label='Simple')
    plt.plot(ticker_df.index, np.log(rendement+1), linestyle='dashed', marker='o', color ='m', label='Log')
    st.plotly_chart(fig)    
    
def computeSMA(data, window):
    # simple moving average
    sma = data.rolling(window=window).mean()
    return sma

def computeEMA(data, span):
    # simple moving average
    ema = data.ewm(span=span, adjust=False).mean()
    return ema

def construct_df(ticker_df):
    
    #get data from yahoo API
    df = ticker_df
    # compute both types of moving averages
    for i in range(50, 250, 50):
        #print(i)
        df['SMA_{}'.format(i)] = computeSMA(df['Adj Close'], i)
    for i in range(50, 250, 50):
        #print(i)
        df['EMA_{}'.format(i)] = computeEMA(df['Adj Close'], i)

        return df  
    
def plot_data_SMA(ticker_df):
    st.header('Moyennes mobiles simples')
    plt.title('Price chart (Adj_Close)')
    plt.plot(ticker_df.index, ticker_df['Adj Close'])

    for i in range(50, 250, 50):
        fig, ax=plt.subplots(figsize=(10,5))
        plt.plot(ticker_df.index, computeSMA(ticker_df['Adj Close'], i), label='SMA_{}'.format(i))

    plt.legend(loc='best')
    st.pyplot(fig)
    
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
    list_action_ticker_standard = ('goog', 'aapl', 'fb', 'nflx', str(tickerSymbol)) # , str(tickerData)
    ticker_df = yf.download(list_action_ticker_standard, start=start_date, end=end_date)
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
    fig_0 = qf.iplot(asFigure=True)
    st.plotly_chart(fig_0)
    ####
    # Rendement 
    stock_data(ticker_df)
    
    # moyenne mobile simple
    plot_data_SMA(ticker_df)
    
    # Courbe des tendance
    # Evolution du cours de l'action 
    st.header("Evolution du cours de l'action")
    ticker_df.index
    fig, ax = plt.subplots(figsize=(12,6))
    ticker_df=ticker_df.asfreq('B')
    plt.plot(ticker_df.index, ticker_df['Close'].shift(-90))
    plt.plot(ticker_df.index, ticker_df['Close'].shift(90))
    plt.plot(ticker_df.index, ticker_df)
    st.pyplot(fig)    
    
    ### st.write(tickerData.info['financialCurrency'])
    