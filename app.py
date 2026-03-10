import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Algorithmic Trading Dashboard")

stock = yf.Ticker("AAPL")
data = stock.history(period="1d", interval="1m")

data['momentum'] = data['Close'].pct_change()

fig = make_subplots(rows=2, cols=1)

fig.add_trace(go.Scatter(
    x=data.index,
    y=data['Close'],
    name='Close Price'
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=data.index,
    y=data['momentum'],
    name='Momentum'
), row=2, col=1)

fig.add_trace(go.Scatter(
    x=data.loc[data['momentum'] > 0].index,
    y=data.loc[data['momentum'] > 0]['Close'],
    mode='markers',
    name='Buy',
    marker=dict(color='green', symbol='triangle-up')
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=data.loc[data['momentum'] < 0].index,
    y=data.loc[data['momentum'] < 0]['Close'],
    mode='markers',
    name='Sell',
    marker=dict(color='red', symbol='triangle-down')
), row=1, col=1)

st.plotly_chart(fig)