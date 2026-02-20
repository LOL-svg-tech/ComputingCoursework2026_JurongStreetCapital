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
        st.warning(f"Please fill all fields correctly")


def limitOrder():
    side = OrderSide.BUY if orderSide == "Buy" else OrderSide.SELL
    req = limitOrderRequest(sym, qty, side, float(lmtPrice), tif)
    try:
        client.submit_order(order_data=req)
    except APIError as e:
        st.warning("Fill all fields correctly")


account = client.get_account()
account_data = Util.to_dataframe(account)
bal_chg = float(account.equity) - float(account.last_equity)
bal = float(account.equity)
positions = Util.to_dataframe(client.get_all_positions())
orders = Util.to_dataframe(client.get_orders())
cum_chg = float(account.equity) - float(100000)

##Sidebar Elements
try:
    sym = st.sidebar.text_input("Insert sym", "DLTR")
except:
    st.error("insert a valid symbol pls")

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
if bal_chg >= 0:
    st.markdown(
        f"**Today's P/L:** :green[$ {bal_chg:.2f}], **Cumulative P/L** :green[${cum_chg:.2f}]"
    )
else:
    st.markdown(
        f"**Today's P/L:** :red[$ {bal_chg:.2f}], **Cumulative P/L** :red[${cum_chg:.2f}]"
    )

st.subheader(f"Current Price: {float(sym_info.fast_info.last_price):.2f}")
# TOP OF THE PAGE THINGS -----------


## Charts
mthly = date.today() - timedelta(days=30)  # Display 30 days
mthly_indicators = date.today() - timedelta(days=180)  # Get 180 days for MACD

request_params = StockBarsRequest(
    symbol_or_symbols=sym,
    timeframe=TimeFrame.Day,
    start=mthly,
)

request_params_indicators = StockBarsRequest(
    symbol_or_symbols=sym,
    timeframe=TimeFrame.Day,
    start=mthly_indicators,
)


bars = dataclient.get_stock_bars(request_params)
data = bars.df
data = data.reset_index()

bars_indicators = dataclient.get_stock_bars(request_params_indicators)
data_indicators = bars_indicators.df.reset_index()

candlestick = go.Candlestick(
    x=data["timestamp"],
    open=data["open"],
    high=data["high"],
    low=data["low"],
    close=data["close"],
)

layout = go.Layout(
    title=f"30 Day Candlestick Chart for {sym}",
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

if show_bollinger:
    bbands_df = bbands_func(close)
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        row_heights=[0.7, 0.3],
        subplot_titles=(f"Candlestick Chart for {sym}", "Bollinger Bands"),
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
    fig.update_layout(title=f"30 Day Candlestick Chart for {sym}")

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
        st.plotly_chart(macd_fig)


## Orders table
st.write("Current Orders")
try:
    st.dataframe(
        orders[["symbol", "side", "qty", "status", "time_in_force"]].rename(
            columns={
                "symbol": "Symbol",
                "qty": "Qty",
                "status": "Status",
                "time_in_force": "Time-In-Force",
            }
        )
    )
except:
    st.dataframe(orders)
st.write("Current Positions")
try:
    st.dataframe(
        positions[["symbol", "side", "qty"]].rename(
            columns={"symbol": "Symbol", "qty": "Qty", "side": "Side"}
        )
    )

except:
    st.dataframe(positions)


st.write(account_data)
