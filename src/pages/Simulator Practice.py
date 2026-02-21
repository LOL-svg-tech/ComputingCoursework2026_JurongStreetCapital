import numpy as np
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.common.exceptions import APIError
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest, StockBarsRequest
from alpaca.data import TimeFrame
import pandas_ta as ta
from datetime import datetime, timedelta, date
from alpaca.data import TimeFrame

dataclient = StockHistoricalDataClient(st.secrets["api_key"], st.secrets["secret_key"])
client = TradingClient(st.secrets["api_key"], st.secrets["secret_key"])
st.title("Terminal")


class Util:  # This was provided by some medium article
    @staticmethod
    def to_dataframe(data):
        if isinstance(data, list):
            return pd.DataFrame([item.__dict__ for item in data])
        return pd.DataFrame(data, columns=["tag", "value"]).set_index("tag")


timeInForce = {
    "Good To Cancel(GTC)": TimeInForce.GTC,
    "Day(DAY)": TimeInForce.DAY,
    "Fill Or Kill(FOK)": TimeInForce.FOK,
    "Immediate Or Cancel(IOC)": TimeInForce.IOC,
    "At The Open(OPG)": TimeInForce.OPG,
    "At The Close(CLS)": TimeInForce.CLS,
}

sym_map = {"Jurong Street Capital": "SPY",
              "SST Robotics": "AMD",
              "SST Computing": "MSFT",
              "SST Electronics": "NVDA",
              "SST Taekwondo":"PLTR"
              
}

rev_sym_map = {val: key for key, val in sym_map.items()}


def marketOrderRequest(sym, qty, side, tif):
    return MarketOrderRequest(
        symbol=sym, qty=qty, side=side, time_in_force=timeInForce[tif]
    )


def limitOrderRequest(sym, qty, side, lmtPrice, tif):
    return LimitOrderRequest(
        symbol=sym,
        qty=qty,
        side=side,
        limit_price=lmtPrice,
        time_in_force=timeInForce[tif],
    )


def marketOrder():
    side = OrderSide.BUY if orderSide == "Buy" else OrderSide.SELL
    req = marketOrderRequest(sym, qty, side, tif)
    try:
        client.submit_order(order_data=req)
    except APIError as e:
        st.warning(f"Please fill all fields correctly {e}")


def limitOrder():
    side = OrderSide.BUY if orderSide == "Buy" else OrderSide.SELL
    req = limitOrderRequest(sym, qty, side, round(float(lmtPrice),2), tif)
    try:
        client.submit_order(order_data=req)
    except APIError as e:
        st.warning(f"Fill all fields correctly {e}")

def symHider(df):
    if df is None or df.empty:
        return df
    displayed = df.copy()
    if "symbol" in displayed.columns:
        displayed["symbol"] = (
            displayed["symbol"]
            .map(rev_sym_map)
            .fillna("Restricted")
        )
    displayed= displayed.rename(columns={"symbol": "Company"})
    return displayed

@st.cache_data(ttl=60)
def getBars(symbol, start):
    req = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Minute,
        start=start,
        limit=600
    )
    return dataclient.get_stock_bars(req).df.reset_index()

@st.cache_data(ttl=5)
def getOrders():
    return Util.to_dataframe(client.get_orders())

@st.cache_data(ttl=5)
def getPositions():
    return Util.to_dataframe(client.get_all_positions())

@st.cache_data(ttl=5)
def getAccount():
    return client.get_account()




account = getAccount()
account_data = Util.to_dataframe(account)
bal_chg = float(account.equity) - float(account.last_equity)
bal = float(account.equity)
positions = symHider(getPositions())
orders = symHider(getOrders())
cum_chg = float(account.equity) - float(100000)



##Sidebar Elements

choice = st.sidebar.selectbox("Select a Company",list(sym_map.keys()))
sym = sym_map[choice]
sym_info = yf.Ticker(sym)
orderSide = st.sidebar.selectbox("Select Order Side", ["Buy", "Sell"])
orderType = st.sidebar.selectbox("Select Order Type", ["Limit(LMT)", "Market(MKT)"])
if orderType == "Limit(LMT)":
    lmtPrice = st.sidebar.number_input(
        "Enter Limit Price", value=sym_info.fast_info.last_price
    )
tif = st.sidebar.selectbox("Time In Force", list(timeInForce))
qty = st.sidebar.number_input("Select Qty (Fractional orders are DAY only)")
st.sidebar.button(
    "Send order", on_click=limitOrder if orderType == "Limit(LMT)" else marketOrder
)
if st.sidebar.toggle("Auto-Refresh"):
    st_autorefresh(interval=5000)

# TOP OF THE PAGE THINGS ------------
st.subheader(f"Current Portfolio Value: USD{bal:.2f}")
if bal_chg >= 0 and cum_chg >= 0:
    st.markdown(
        f"**Today's P/L:** :green[$ {bal_chg:.2f}], **Cumulative P/L** :green[${cum_chg:.2f}]"
    )
elif bal_chg >= 0 and cum_chg <= 0:
    st.markdown(
        f"**Today's P/L:** :green[$ {bal_chg:.2f}], **Cumulative P/L** :red[${cum_chg:.2f}]"
    )
elif bal_chg <= 0 and cum_chg >= 0:
    st.markdown(
        f"**Today's P/L:** :red[$ {bal_chg:.2f}], **Cumulative P/L** :green[${cum_chg:.2f}]"
    )
else:
    st.markdown(
        f"**Today's P/L:** :red[$ {bal_chg:.2f}], **Cumulative P/L** :red[${cum_chg:.2f}]"
    )

st.subheader(f"Current Price: {float(sym_info.fast_info.last_price):.2f}")
# TOP OF THE PAGE THINGS -----------


## Charts
start = date.today() - timedelta(days=1)  # Display 3 days
start_indicators = date.today() - timedelta(days=2)  # Get 30 days for MACD



data = getBars(sym, start).set_index('timestamp').resample('5min').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum'
}).fillna(method="ffill").reset_index()

data_indicators = getBars(sym, start_indicators).set_index('timestamp').resample('5min').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum'
}).dropna().reset_index()



candlestick = go.Candlestick(
    x=data["timestamp"],
    open=data["open"],
    high=data["high"],
    low=data["low"],
    close=data["close"],
)

layout = go.Layout(
    title=f"30 Day Candlestick Chart for {choice}",
    xaxis=dict(title="Date"),
    yaxis=dict(title="Price"),
)

# INDICATORS
show_rsi = st.checkbox("Show RSI")
show_macd = st.checkbox("Show MACD")
show_bollinger = st.checkbox("Show Bollinger Bands")

from pandas_ta.momentum import macd as macd_func
from pandas_ta.momentum import rsi as rsi_func
from pandas_ta.volatility import bbands as bbands_func
from plotly.subplots import make_subplots

close = data["close"]
close_indicators = data_indicators["close"]

rangebreaks = [
    dict(bounds=["sat", "mon"]),   
    dict(bounds=[16, 9.5], pattern="hour") 
]

##This was modified to work with the help of AI Model Big Pickle
if show_bollinger:
    bbands_df = bbands_func(close)
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        row_heights=[0.7, 0.3],
        subplot_titles=(f"5min Candlestick Chart for {choice}"),
    )
    fig.add_trace(
        go.Candlestick(
            x=data["timestamp"],
            open=data["open"],
            high=data["high"],
            low=data["low"],
            close=data["close"],
            name="Price",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=data["timestamp"],
            y=bbands_df["BBL_5_2.0_2.0"],
            mode="lines",
            name="Lower Band",
            line=dict(color="red", width=1),
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=data["timestamp"],
            y=bbands_df["BBU_5_2.0_2.0"],
            mode="lines",
            name="Upper Band",
            line=dict(color="red", width=1),
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=data["timestamp"],
            y=bbands_df["BBM_5_2.0_2.0"],
            mode="lines",
            name="Middle Band",
            line=dict(color="blue", width=1),
        ),
        row=1,
        col=1,
    )
else:
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data["timestamp"],
                open=data["open"],
                high=data["high"],
                low=data["low"],
                close=data["close"],
            )
        ]
    )
    fig.update_layout(title=f"5min Candlestick Chart for {choice}")

fig.update_xaxes(rangebreaks=rangebreaks)
st.plotly_chart(fig)

if show_rsi:
    rsi_data = rsi_func(close)
    if rsi_data is not None:
        rsi_fig = go.Figure()
        rsi_fig.add_trace(
            go.Scatter(
                x=data["timestamp"],
                y=rsi_data,
                mode="lines",
                name="RSI",
                line=dict(color="purple"),
            )
        )
        rsi_fig.add_hline(y=70, line_color="red", line_dash="dash")
        rsi_fig.add_hline(y=30, line_color="green", line_dash="dash")
        rsi_fig.update_yaxes(range=[0, 100])
        rsi_fig.update_layout(height=250, title="RSI")
        rsi_fig.update_xaxes(rangebreaks=rangebreaks)
        st.plotly_chart(rsi_fig)

if show_macd:
    macd_data = macd_func(close_indicators)
    if macd_data is not None:
        macd_fig = go.Figure()
        macd_fig.add_trace(
            go.Scatter(
                x=data_indicators["timestamp"],
                y=macd_data["MACD_12_26_9"],
                mode="lines",
                name="MACD Line",
                line=dict(color="blue"),
            )
        )
        macd_fig.add_trace(
            go.Scatter(
                x=data_indicators["timestamp"],
                y=macd_data["MACDs_12_26_9"],
                mode="lines",
                name="Signal Line",
                line=dict(color="orange"),
            )
        )
        macd_fig.update_layout(height=250, title="MACD")
        macd_fig.update_xaxes(rangebreaks=rangebreaks)
        st.plotly_chart(macd_fig)
##This was modified to work with the help of AI Model Big Pickle

## Orders table
st.write("Current Orders")
try:
    st.dataframe(
        orders[["Company", "side", "qty", "status", "time_in_force","filled_avg_price","limit_price","order_type"]].rename(
            columns={
                "Company": "Company",
                "qty": "Qty",
                "filled_avg_price":"Avg. Fill Price",
                "limit_price":"Limit Price",
                "status": "Status",
                "time_in_force": "Time-In-Force",
                "order_type":"Order Type"
            }
        )
    )
except:
    st.dataframe(orders)
st.write("Current Positions")
try:
    st.dataframe(
        positions[["Company", "avg_entry_price","unrealized_pl","side", "qty"]].rename(
            columns={"Company": "Company","avg_entry_price":"Avg. Cost Price","unrealized_pl":"Unrealized P/L","qty": "Qty", "side": "Side"}
        )
    )

except:
    st.dataframe(positions)



st.write("Account Data")
st.write(account_data)

