import pandas as pd
import numpy as np
import datetime
import investpy
import wbgapi

#downloading datasets to test on

today = datetime.datetime.today().strftime('%d/%m/%Y')
def stockdata(ticker1='AAPL', ticker2='MSFT', startdate='01/01/2020', enddate=today):
    df = investpy.stocks.get_stock_historical_data(ticker1, country='United States', from_date=startdate, to_date=enddate)
    return df