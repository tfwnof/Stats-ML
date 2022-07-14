import pandas as pd
import numpy as np
import datetime as dt
import investpy
import wbgapi

#default end dates will be today
today = dt.datetime.today().strftime('%d/%m/%Y')

#get stock data
def stockdata(ticker='AAPL', listed='United States', startdate='01/01/2020', enddate=today):
    df = investpy.stocks.get_stock_historical_data(ticker, country=listed, from_date=startdate, to_date=enddate)
    return df

