import pandas as pd

prices = pd.read_csv('./data/prices.csv', index_col=[0,1], parse_dates=[1])

def stock_prices(symbol):
  return prices.loc[symbol].copy()
