import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import talib

st.title("Stock Portfolio Dashboard")

selected_ticker = st.selectbox("Choose a stock", ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'META', 'NVDA', 'TSLA'])

df = pd.read_csv(f"./data/{selected_ticker}_historical_data.csv", parse_dates=['Date'], index_col='Date')
df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)

st.line_chart(df[['Close', 'SMA_20']])
st.line_chart(df['RSI'])
