#import streamlit as st
import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import string
import random

# BasePage
class Scrapper():
    def __init__(self):
        pass
        
    def web_content_div(self, content, class_path):
        content = content.find_all('div', attrs={'class': class_path}) 
        try:
            streamers = content[0].find_all('fin-streamer')
            texts = [streamer.get_text() for streamer in streamers if streamer != '']
        except IndexError:
            texts = []
        
        return texts        

    def real_time_price(self, stock_code):
        url = 'https://finance.yahoo.com/quote/'+ stock_code +'?p='+ stock_code + '&.tsrc=fin-srch'
        volume = []
        one_year_target = []
        lastest_pattern = []
        try:
            r = requests.get(url)
            content = BeautifulSoup(r.text, 'lxml')
            texts = self.web_content_div(content, 'My(6px) Pos(r) smartphone_Mt(6px) W(100%)')
            if texts != []:
                price, change = texts[0], texts[1] +' '+ texts[2]
            else:
                price, change = [], []
            texts = content.find_all('div', attrs={'class': 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'})
            if texts != []:
                volume = texts[0].find('td', attrs={'data-test':'TD_VOLUME-value'}).get_text()
            else:
                volume = []

            pattern = self.web_content_div(content, 'Fz(xs) Mb(4px)')
            try:
                lastest_pattern = pattern[0]
            except IndexError:
                lastest_pattern = []

            texts = content.find_all('div', attrs={'class':'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)'})
            if texts != []:
                one_year_target = texts[0].find('td', attrs={'data-test':'ONE_YEAR_TARGET_PRICE-value'}).get_text()
            else:
                one_year_target = []
        except ConnectionError:
            price, change, volume, lastest_pattern, one_year_target = [], [], [], [], []
        
        return price, change, volume, lastest_pattern, one_year_target
 
    def runner(self):
        stock = ['BRK-B', 'PYPL', 'TWTR', 'AAPL', 'AMZN', 'MSFT', 'FB', 'GOOG']

        while (True):
            info = []
            col = []
            time_stamp = datetime.datetime.now() - datetime.timedelta(hours=13)
            time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
            for stock_code in stock:
                price, change, volume, lastest_pattern, one_year_target = self.real_time_price(stock_code)        
                info.append(price)
                info.extend([change])
                info.extend([volume])
                info.extend([lastest_pattern])
                info.extend([one_year_target])
            col = [time_stamp]
            col.extend(info)
            df = pd.DataFrame(col)
            df = df.T
            df.to_csv('data/' + str(time_stamp[0:11]) + 'stock data.csv', mode='a', header=False)
            print(col)
            
    


if __name__ == '__main__':
    home = HomePage()
    #print(home.real_time_price('BRK-B'))
    stock = ['BRK-B', 'PYPL', 'TWTR', 'AAPL', 'AMZN', 'MSFT', 'FB', 'GOOG']

    while (True):
        info = []
        col = []
        time_stamp = datetime.datetime.now() - datetime.timedelta(hours=13)
        time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
        for stock_code in stock:
            price, change, volume, lastest_pattern, one_year_target = home.real_time_price(stock_code)        
            info.append(price)
            info.extend([change])
            info.extend([volume])
            info.extend([lastest_pattern])
            info.extend([one_year_target])
        col = [time_stamp]
        col.extend(info)
        df = pd.DataFrame(col)
        df = df.T
        df.to_csv(str(time_stamp[0:11]) + 'stock data.csv', mode='a', header=False)
        print(col)
        





