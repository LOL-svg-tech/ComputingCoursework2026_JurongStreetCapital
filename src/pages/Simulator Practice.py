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
        df = pd.DataFrame(
            [(k, str(v)) for k, v in data.__dict__.items()], columns=["tag", "value"]
        ).set_index("tag")
        return df


timeInForce = {
    "Good To Cancel(GTC)": TimeInForce.GTC,
    "Day(DAY)": TimeInForce.DAY,
    "Fill Or Kill(FOK)": TimeInForce.FOK,
    "Immediate Or Cancel(IOC)": TimeInForce.IOC,
    "At The Open(OPG)": TimeInForce.OPG,
    "At The Close(CLS)": TimeInForce.CLS,
}
# Dictionary mapping different TIFs to text to use in a dropdown

sym_map = {
    "Jurong Street Capital": "SPY",
    "SST Robotics": "AMD",
    "SST Computing": "MSFT",
    "SST Electronics": "NVDA",
    "SST Taekwondo": "PLTR",
}

# Mapping each symbol to fictional company names, so that the user has to really rely solely on skills learnt in modules to trade, not using news or any other alpha

# This reverses the key value pair 
rev_sym_map = {val: key for key, val in sym_map.items()}

# A function to wrap and return s MarketOrderRequest method
def marketOrderRequest(sym, qty, side, tif):
    return MarketOrderRequest(
        symbol=sym, qty=qty, side=side, time_in_force=timeInForce[tif]
    )

# A function to wrap and return Alpaca's LimitOrderRequest method
def limitOrderRequest(sym, qty, side, lmtPrice, tif):
    return LimitOrderRequest(
        symbol=sym,
        qty=qty,
        side=side,
        limit_price=lmtPrice,
        time_in_force=timeInForce[tif],
    )

# A function to utilise marketorderequest and submit mktrequest data to alpaca 
def marketOrder():
    side = OrderSide.BUY if orderSide == "Buy" else OrderSide.SELL
    req = marketOrderRequest(sym, qty, side, tif)
    try:
        client.submit_order(order_data=req)
    except APIError as e:
        st.warning(f"Please fill all fields correctly {e}")

# A function to utilise limitorderequest and submit mktrequest data to alpaca f
def limitOrder():
    side = OrderSide.BUY if orderSide == "Buy" else OrderSide.SELL
    req = limitOrderRequest(sym, qty, side, round(float(lmtPrice), 2), tif)
    try:
        client.submit_order(order_data=req)
    except APIError as e:
        st.warning(f"Fill all fields correctly {e}")

# Hides the synbol names in tables to prevents users from finding out through posiitions/order table to see what irl symbol they bought/sold
def symHider(df):
    if df is None or df.empty:
        return df
    displayed = df.copy()
    if "symbol" in displayed.columns:
        displayed["symbol"] = displayed["symbol"].map(rev_sym_map).fillna("Restricted")
    displayed = displayed.rename(columns={"symbol": "Company"})
    return displayed

# Using cache data for efficiency to prevent unnecessary reruns, and using yf.download to obtain ticker data
@st.cache_data(ttl=60)
def getBars(symbol):
    df = yf.download(symbol, period="2d", interval="5m", progress=False)
    df.index = df.index.tz_convert("America/New_York")
    return df

# Using cache data for efficiency to prevent unnecessary reruns to get orders from alpaca
@st.cache_data(ttl=5)
def getOrders():
    return Util.to_dataframe(client.get_orders())

# Using cache data for efficiency to prevent unnecessary reruns to get positions from alpaca
@st.cache_data(ttl=5)
def getPositions():
    return Util.to_dataframe(client.get_all_positions())

# Using cache data for efficiency to prevent unnecessary reruns to get Account data from alpaca
@st.cache_data(ttl=5)
def getAccount():
    return client.get_account()


account = getAccount() # Get alpaca data
account_data = Util.to_dataframe(account) # Using the goated medium function to convert all the dict data to df
bal_chg = float(account.equity) - float(account.last_equity) # get daily balance change in float
bal = float(account.equity) # get daily balance
positions = symHider(getPositions()) # Using symhider to mask sym position name
orders = symHider(getOrders()) # using symhider to mask sym position names
cum_chg = float(account.equity) - float(100000) # cumulative change of port value (hardcoded 100000 since acc started with 100000)

# A bunch of variables computed from alpaca data

##Sidebar Elements


choice = st.sidebar.selectbox("Select a Company", list(sym_map.keys())) # Using list to sym_map.keys() to display as a dropdown
sym = sym_map[choice] # get actual symbol by referencing dict with choice
sym_info = yf.Ticker(sym) # Quickly get symbol data with yf.ticker
orderSide = st.sidebar.selectbox("Select Order Side", ["Buy", "Sell"]) 
orderType = st.sidebar.selectbox("Select Order Type", ["Limit(LMT)", "Market(MKT)"])

#Dropdowns of ordertype order side, time in force
if orderType == "Limit(LMT)":
    lmtPrice = st.sidebar.number_input(
        "Enter Limit Price", value=sym_info.fast_info.last_price
    )
tif = st.sidebar.selectbox("Time In Force", list(timeInForce)) #
qty = st.sidebar.number_input("Select Qty (Fractional orders are DAY only)") #order qty
st.sidebar.button(
    "Send order", on_click=limitOrder if orderType == "Limit(LMT)" else marketOrder
)
if st.sidebar.toggle("Auto-Refresh"): # Autorefresh function
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

# abunch of if else for PnL colors

st.subheader(f"Current Price: {float(sym_info.fast_info.last_price):.2f}") #using fast info to get current price
# TOP OF THE PAGE THINGS -----------


## Charts

data = getBars(sym) # calling func getbars to get symbol data


# INDICATORS
# Checkboxes to display each TA indicator
show_rsi = st.checkbox("Show RSI")
show_macd = st.checkbox("Show MACD")
show_bollinger = st.checkbox("Show Bollinger Bands")


from pandas_ta.momentum import macd as macd_func
from pandas_ta.momentum import rsi as rsi_func
from pandas_ta.volatility import bbands as bbands_func
from plotly.subplots import make_subplots

close = data[("Close", sym)]
# The rangebreaks is to deal with null/blank data in time
rangebreaks = [dict(bounds=["sat", "mon"]), dict(bounds=[16, 9.5], pattern="hour")]

##This was modified to work with the help of AI Model Big Pickle
# Create the macd graph, plotting the macd and signal line. And also altering the height to 300
if show_bollinger:
    bbands_df = bbands_func(close)
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        row_heights=[0.7, 0.3],
        subplot_titles=(f"5m Candlestick Chart for {choice}"),
    )
    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data[("Open", sym)],
            high=data[("High", sym)],
            low=data[("Low", sym)],
            close=data[("Close", sym)],
            name="Price",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=data.index,
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
            x=data.index,
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
            x=data.index,
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
                x=data.index,
                open=data[("Open", sym)],
                high=data[("High", sym)],
                low=data[("Low", sym)],
                close=data[("Close", sym)],
            )
        ]
    )
    fig.update_layout(title=f"5m Candlestick Chart for {choice}")

fig.update_xaxes(rangebreaks=rangebreaks)
st.plotly_chart(fig)
# Create the rsi graph, adding the 70 and 30 levels. And also altering the height to 300
if show_rsi:
    rsi_data = rsi_func(close)
    if rsi_data is not None:
        rsi_fig = go.Figure()
        rsi_fig.add_trace(
            go.Scatter(
                x=data.index,
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
# If the checkbox for bollinger is ticked, then display the bollinger.
# The bollinger is directly on the candlestick, therefore we do initial_candle_fig.add_trace().
# initial_candle_fig is the first graph they see before choosing their option
if show_macd:
    macd_data = macd_func(close)
    if macd_data is not None:
        macd_fig = go.Figure()
        macd_fig.add_trace(
            go.Scatter(
                x=data.index,
                y=macd_data["MACD_12_26_9"],
                mode="lines",
                name="MACD Line",
                line=dict(color="blue"),
            )
        )
        macd_fig.add_trace(
            go.Scatter(
                x=data.index,
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
try:  # Only display certain parts of the position that user will understand
    st.dataframe(
        orders[
            [
                "Company",
                "side",
                "qty",
                "status",
                "time_in_force",
                "filled_avg_price",
                "limit_price",
                "order_type",
            ]
        ].rename(
            columns={
                "Company": "Company",
                "qty": "Qty",
                "filled_avg_price": "Avg. Fill Price",
                "limit_price": "Limit Price",
                "status": "Status",
                "time_in_force": "Time-In-Force",
                "order_type": "Order Type",
            }
        )
    )
except:
    # Display none if fields are not present
    st.dataframe(orders)
st.write("Current Positions")
# Using a try-except block to only display
try:  # Only display certain parts of the position that user will understand
    st.dataframe(
        positions[
            ["Company", "avg_entry_price", "unrealized_pl", "side", "qty"]
        ].rename(
            columns={
                "Company": "Company",
                "avg_entry_price": "Avg. Cost Price",
                "unrealized_pl": "Unrealized P/L",
                "qty": "Qty",
                "side": "Side",
            }
        )
    )

except:
    # Display none if fields are not present
    st.dataframe(positions)


st.write("Account Data")
# Display verbose account data
st.write(account_data)
