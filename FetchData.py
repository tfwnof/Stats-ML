from datetime import datetime, timedelta
import investpy
import wbgapi

#default dates
today = datetime.date(datetime.now()).strftime('%d/%m/%Y')
trailingYear = datetime.date(datetime.now()) - timedelta(days=365)
trailingYear = trailingYear.strftime('%d/%m/%Y')

#get stock data - Loading by default Apple's historical data
def stockdata(ticker='AAPL', listed='United States', startdate=trailingYear, enddate=today):
    df = investpy.stocks.get_stock_historical_data(ticker, country=listed, from_date=startdate, to_date=enddate)
    return df

#get indexes
def stocksindex():
    df = investpy.indices.get_index_historical_data('NQ US 300', country='United States', from_date=trailingYear, to_date=today)
    return df

#get GDP
def Econdata():
    return
