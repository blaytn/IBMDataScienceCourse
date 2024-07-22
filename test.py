import yfinance as yf
import plotly.express as px
import pandas as pd

t = yf.Ticker('AAPL')
t_data = t.history(period='1d', interval='1m')

data = pd.DataFrame(t_data)
print(data)
