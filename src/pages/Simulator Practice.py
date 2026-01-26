import numpy as np
import pandas as pd 
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.common.exceptions import APIError
import yfinance as yf




client = TradingClient(st.secrets["api_key"], st.secrets["secret_key"])
st.title("Terminal")

class Util: #This was provided by some medium article
    @staticmethod
    def to_dataframe(data):
        if isinstance(data, list):
            return pd.DataFrame([item.__dict__ for item in data])
        return pd.DataFrame(data, columns=['tag', 'value']).set_index('tag')
    
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

def limitOrderRequest(sym, qty, side, lmtPrice ,tif):
    return LimitOrderRequest(
        symbol = sym, qty = qty, side = side, limit_price = lmtPrice, time_in_force=timeInForce[tif]
    )
def marketOrder():
    side = OrderSide.BUY if orderSide=="Buy" else OrderSide.SELL
    req  = marketOrderRequest(
        sym,
        qty,
        side,
        tif  
    )
    try:
        client.submit_order(order_data=req)
    except APIError as e:
            st.warning(f"Please fill all fields correctly")
        
    
def limitOrder():
    side = OrderSide.BUY if orderSide=="Buy" else OrderSide.SELL
    req = limitOrderRequest(
        sym,
        qty,
        side,
        float(lmtPrice),
        tif
    )
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


#TOP OF THE PAGE THINGS ------------
st.subheader(f"Current Portfolio Value: USD{bal:.2f}")
if bal_chg >= 0:
    st.markdown(f"**Today's P/L:** :green[$ {bal_chg:.2f}]")
else:
    st.markdown(f"**Today's P/L:** :red[$ {bal_chg:.2f}]")
#TOP OF THE PAGE THINGS -----------



##Sidebar Elements
try:
    sym = st.sidebar.text_input("Insert Ticker", "SPY")
except:
    st.error("insert a valid symbol pls")

sym_info = yf.Ticker(sym)
orderSide = st.sidebar.selectbox("Select Order Side", ["Buy","Sell"])
orderType = st.sidebar.selectbox("Select Order Type", ["Limit(LMT)", "Market(MKT)"])
if orderType == "Limit(LMT)":
    lmtPrice = st.sidebar.number_input("Enter Limit Price", value=sym_info.fast_info.last_price)
tif = st.sidebar.selectbox("Time In Force", list(timeInForce))
qty = st.sidebar.number_input("Select Qty (Fractional orders are DAY only)")
st.sidebar.button("Send order",on_click=limitOrder if orderType=="Limit(LMT)" else marketOrder)


## Orders table
try:
    st.dataframe(orders[["symbol","side","qty","status","time_in_force"]].rename(columns={"symbol":"Symbol","qty":"Qty","status":"Status","time_in_force":"Time-In-Force"}))
except:
    st.dataframe(orders)
try:
    st.dataframe(positions[["symbol","side","qty"]].rename(columns={"symbol":"Symbol","qty":"Qty","side":"Side"}))

except:
    st.dataframe(positions)







st.write(account_data)



