import streamlit as st
import yfinance as yf
import random
import plotly.graph_objects as go
import pandas_ta as ta
import pandas as pd

# This entire section is just UI

st.title("Let's learn Trade!")

st.divider()

st.header("Article 3: Indicator-Based Trading")

st.subheader(
    "Indicators are not magic. Past performance does not guarantee future results."
)
st.subheader("Indicators vs Reality: What do they actually do?")
st.write(
    "Indicators apply math to historical market data in order for traders to understand what is going on."
)
st.markdown("""
Indicators are based on **past data**, which means:
- They **summarize historical prices**.
- They can indicate **volatility or momentum**.
- They are inherently **lagging**, not predictive.
""")
st.write("This means that indicators should be used as tools, and not as prophecies.")

st.divider()
st.subheader("Different Types of Indicators")
rsi, macd, bollinger = st.tabs(
    [
        "Relative Strength Index",
        "Moving Average Convergence Divergence",
        "Bollinger Bands",
    ]
)
with rsi:
    st.markdown("### Relative Strength Index (RSI)")
    st.write("""
    The **Relative Strength Index (RSI)** is a momentum indicator that measures the speed and magnitude of which a price changes.
    When price goes too quickly and too far in one direction, it tends to want to go to the other way. This is known as a reversal.
    - RSI above 70 → generally considered overbought (possible reversal down)
    - RSI below 30 → generally considered oversold (possible reversal up)
             
    RSI is generally used in reversal strategies, where they see the market move in one direction, and what to profit from a price reversal, which is usually very strong
    """)
with macd:
    st.markdown("### Moving Average Convergence Divergence (MACD)")
    st.write("""
    The **Moving Average Convergence Divergence (MACD)** is a technical indicator that uses moving averages across different time periods, with values from 0 to 100.
    It subtracts the exponential moving average of a longer time period (usually 26 months) from the exponential moving average of a shorter time period (usually 12 months) to get the MACD line.
    - MACD line crosses above signal line → bullish signal 
    - MACD line crosses below signal line → bearish signal
    
    The signal line is the EMA of the MACD line. When the MACD is above the signal line, it indicates upward momentum; when it is below, momentum is weakening.
    """)
with bollinger:
    st.markdown("### Bollinger Bands")
    st.markdown("""
    **Bollinger Bands** measure market **volatility** by plotting standard deviation bands around a moving average.
    The indicator has 3 lines: 
    - An upper and lower band represent the upper and lower ends of the prices respective
    - A moving average in the centre
                
    Here is how it is typically read:
    - Price touches upper band → potentially overbought
    - Price touches lower band → potentially oversold
    - Bands widening → high volatility
    - Bands contracting → low volatility
    """)
st.divider()
st.subheader("Indicator Confluence")
st.write("""
Relying on **one indicator alone** is risky. If one of the indicators is wrong and you rely solely on it, your trading decision will more often than not be inaccurate.
       
Combining indicators can:
- Reduce false signals
- Confirm trends or reversals
- Provide a more balanced view
""")
st.markdown("""
**Example of Confluence:**  
- RSI is under 30 (Indicates it is oversold)  
- Price touches lower Bollinger Band (Indicates that it is on the lower end of the price range, and oversold)
- MACD shows bullish crossover (Indicates that price wants to go up)
This combination increases the probability of a valid trade setup.
""")
st.divider()
st.subheader("Common Mistakes with Indicators")
st.write("""
Many traders fall into these traps:
- **Indicator stacking:** Using too many indicators can create confusion.
- **Late entries:** Waiting for all indicators to confirm often means entering after most of the move is over.
- **Over-optimization:** Adjusting indicator parameters too closely to past data reduces future reliability.
- **Setting take profits and stop losses incorrectly**
    - Take Profit too far → price may never reach it; Take Profit too close → miss potential gains.
    - Stop Loss too far → risk larger losses; Stop Loss too close → risk being stopped out on a temporary dip.
""")
st.divider()
st.subheader("Interactive Indicator Learning")
st.write(
    "You can experiment with indicators on charts and practice identifying signals."
)

tickers = [
    "MMM",
    "AOS",
    "ABT",
    "ABBV",
    "ACN",
    "ADBE",
    "AMD",
    "AES",
    "AFL",
    "A",
    "APD",
    "ABNB",
    "AKAM",
    "ALB",
    "ARE",
    "ALGN",
    "ALLE",
    "LNT",
    "ALL",
    "GOOGL",
    "GOOG",
    "MO",
    "AMZN",
    "AMCR",
    "AEE",
    "AEP",
    "AXP",
    "AIG",
    "AMT",
    "AWK",
    "AMP",
    "AME",
    "AMGN",
    "APH",
    "ADI",
    "AON",
    "APA",
    "APO",
    "AAPL",
    "AMAT",
    "APP",
    "APTV",
    "ACGL",
    "ADM",
    "ARES",
    "ANET",
    "AJG",
    "AIZ",
    "T",
    "ATO",
    "ADSK",
    "ADP",
    "AZO",
    "AVB",
    "AVY",
    "AXON",
    "BKR",
    "BALL",
    "BAC",
    "BAX",
    "BDX",
    "BRK.B",
    "BBY",
    "TECH",
    "BIIB",
    "BLK",
    "BX",
    "XYZ",
    "BK",
    "BA",
    "BKNG",
    "BSX",
    "BMY",
    "AVGO",
    "BR",
    "BRO",
    "BF.B",
    "BLDR",
    "BG",
    "BXP",
    "CHRW",
    "CDNS",
    "CPT",
    "CPB",
    "COF",
    "CAH",
    "CCL",
    "CARR",
    "CVNA",
    "CAT",
    "CBOE",
    "CBRE",
    "CDW",
    "COR",
    "CNC",
    "CNP",
    "CF",
    "CRL",
    "SCHW",
    "CHTR",
    "CVX",
    "CMG",
    "CB",
    "CHD",
    "CIEN",
    "CI",
    "CINF",
    "CTAS",
    "CSCO",
    "C",
    "CFG",
    "CLX",
    "CME",
    "CMS",
    "KO",
    "CTSH",
    "COIN",
    "CL",
    "CMCSA",
    "FIX",
    "CAG",
    "COP",
    "ED",
    "STZ",
    "CEG",
    "COO",
    "CPRT",
    "GLW",
    "CPAY",
    "CTVA",
    "CSGP",
    "COST",
    "CTRA",
    "CRH",
    "CRWD",
    "CCI",
    "CSX",
    "CMI",
    "CVS",
    "DHR",
    "DRI",
    "DDOG",
    "DVA",
    "DECK",
    "DE",
    "DELL",
    "DAL",
    "DVN",
    "DXCM",
    "FANG",
    "DLR",
    "DG",
    "DLTR",
    "D",
    "DPZ",
    "DASH",
    "DOV",
    "DOW",
    "DHI",
    "DTE",
    "DUK",
    "DD",
    "ETN",
    "EBAY",
    "ECL",
    "EIX",
    "EW",
    "EA",
    "ELV",
    "EME",
    "EMR",
    "ETR",
    "EOG",
    "EPAM",
    "EQT",
    "EFX",
    "EQIX",
    "EQR",
    "ERIE",
    "ESS",
    "EL",
    "EG",
    "EVRG",
    "ES",
    "EXC",
    "EXE",
    "EXPE",
    "EXPD",
    "EXR",
    "XOM",
    "FFIV",
    "FDS",
    "FICO",
    "FAST",
    "FRT",
    "FDX",
    "FIS",
    "FITB",
    "FSLR",
    "FE",
    "FISV",
    "F",
    "FTNT",
    "FTV",
    "FOXA",
    "FOX",
    "BEN",
    "FCX",
    "GRMN",
    "IT",
    "GE",
    "GEHC",
    "GEV",
    "GEN",
    "GNRC",
    "GD",
    "GIS",
    "GM",
    "GPC",
    "GILD",
    "GPN",
    "GL",
    "GDDY",
    "GS",
    "HAL",
    "HIG",
    "HAS",
    "HCA",
    "DOC",
    "HSIC",
    "HSY",
    "HPE",
    "HLT",
    "HOLX",
    "HD",
    "HON",
    "HRL",
    "HST",
    "HWM",
    "HPQ",
    "HUBB",
    "HUM",
    "HBAN",
    "HII",
    "IBM",
    "IEX",
    "IDXX",
    "ITW",
    "INCY",
    "IR",
    "PODD",
    "INTC",
    "IBKR",
    "ICE",
    "IFF",
    "IP",
    "INTU",
    "ISRG",
    "IVZ",
    "INVH",
    "IQV",
    "IRM",
    "JBHT",
    "JBL",
    "JKHY",
    "J",
    "JNJ",
    "JCI",
    "JPM",
    "KVUE",
    "KDP",
    "KEY",
    "KEYS",
    "KMB",
    "KIM",
    "KMI",
    "KKR",
    "KLAC",
    "KHC",
    "KR",
    "LHX",
    "LH",
    "LRCX",
    "LW",
    "LVS",
    "LDOS",
    "LEN",
    "LII",
    "LLY",
    "LIN",
    "LYV",
    "LMT",
    "L",
    "LOW",
    "LULU",
    "LYB",
    "MTB",
    "MPC",
    "MAR",
    "MRSH",
    "MLM",
    "MAS",
    "MA",
    "MTCH",
    "MKC",
    "MCD",
    "MCK",
    "MDT",
    "MRK",
    "META",
    "MET",
    "MTD",
    "MGM",
    "MCHP",
    "MU",
    "MSFT",
    "MAA",
    "MRNA",
    "MOH",
    "TAP",
    "MDLZ",
    "MPWR",
    "MNST",
    "MCO",
    "MS",
    "MOS",
    "MSI",
    "MSCI",
    "NDAQ",
    "NTAP",
    "NFLX",
    "NEM",
    "NWSA",
    "NWS",
    "NEE",
    "NKE",
    "NI",
    "NDSN",
    "NSC",
    "NTRS",
    "NOC",
    "NCLH",
    "NRG",
    "NUE",
    "NVDA",
    "NVR",
    "NXPI",
    "ORLY",
    "OXY",
    "ODFL",
    "OMC",
    "ON",
    "OKE",
    "ORCL",
    "OTIS",
    "PCAR",
    "PKG",
    "PLTR",
    "PANW",
    "PSKY",
    "PH",
    "PAYX",
    "PAYC",
    "PYPL",
    "PNR",
    "PEP",
    "PFE",
    "PCG",
    "PM",
    "PSX",
    "PNW",
    "PNC",
    "POOL",
    "PPG",
    "PPL",
    "PFG",
    "PG",
    "PGR",
    "PLD",
    "PRU",
    "PEG",
    "PTC",
    "PSA",
    "PHM",
    "PWR",
    "QCOM",
    "DGX",
    "Q",
    "RL",
    "RJF",
    "RTX",
    "O",
    "REG",
    "REGN",
    "RF",
    "RSG",
    "RMD",
    "RVTY",
    "HOOD",
    "ROK",
    "ROL",
    "ROP",
    "ROST",
    "RCL",
    "SPGI",
    "CRM",
    "SNDK",
    "SBAC",
    "SLB",
    "STX",
    "SRE",
    "NOW",
    "SHW",
    "SPG",
    "SWKS",
    "SJM",
    "SW",
    "SNA",
    "SOLV",
    "SO",
    "LUV",
    "SWK",
    "SBUX",
    "STT",
    "STLD",
    "STE",
    "SYK",
    "SMCI",
    "SYF",
    "SNPS",
    "SYY",
    "TMUS",
    "TROW",
    "TTWO",
    "TPR",
    "TRGP",
    "TGT",
    "TEL",
    "TDY",
    "TER",
    "TSLA",
    "TXN",
    "TPL",
    "TXT",
    "TMO",
    "TJX",
    "TKO",
    "TTD",
    "TSCO",
    "TT",
    "TDG",
    "TRV",
    "TRMB",
    "TFC",
    "TYL",
    "TSN",
    "USB",
    "UBER",
    "UDR",
    "ULTA",
    "UNP",
    "UAL",
    "UPS",
    "URI",
    "UNH",
    "UHS",
    "VLO",
    "VTR",
    "VLTO",
    "VRSN",
    "VRSK",
    "VZ",
    "VRTX",
    "VTRS",
    "VICI",
    "V",
    "VST",
    "VMC",
    "WRB",
    "GWW",
    "WAB",
    "WMT",
    "DIS",
    "WBD",
    "WM",
    "WAT",
    "WEC",
    "WFC",
    "WELL",
    "WST",
    "WDC",
    "WY",
    "WSM",
    "WMB",
    "WTW",
    "WDAY",
    "WYNN",
    "XEL",
    "XYL",
    "YUM",
    "ZBRA",
    "ZBH",
    "ZTS",
]
# st.session state saves the state of the buttons, so when the app is rerun, our chosen options still remain
st.session_state["rsi"] = st.checkbox("Show RSI")
st.session_state["macd"] = st.checkbox("Show MACD")
st.session_state["bbands"] = st.checkbox("Show Bollinger Bands")
show_rsi = st.session_state["rsi"]
show_macd = st.session_state["macd"]
show_bollinger = st.session_state["bbands"]

# checks if there is a ticker saved, if there is none, then randomly generate a ticker and save it
if "ticker" not in st.session_state:
    st.session_state["ticker"] = random.choice(tickers)

# Gets the data for the ticker from yfinance
ticker = st.session_state["ticker"]
five_day_data = yf.download(ticker, period="5d", interval="5m")
five_day_data.index = five_day_data.index.tz_convert("America/New_York")
unique_dates = pd.Series(five_day_data.index.date).unique()

# Gets the second last date, because we display the second last date from today on the candlesticks
second_last_date = unique_dates[-2]
second_last_day_data = five_day_data[five_day_data.index.date == second_last_date]

# Create the candlestick graph
initial_candle_fig = go.Figure(
    data=[
        go.Candlestick(
            x=second_last_day_data.index,
            open=second_last_day_data[("Open", ticker)],
            high=second_last_day_data[("High", ticker)],
            low=second_last_day_data[("Low", ticker)],
            close=second_last_day_data[("Close", ticker)],
            name="Candles",
        )
    ],
    layout=go.Layout(height=500),
)

# Create the rsi graph, adding the 70 and 30 levels. And also altering the height to 300
rsi_fig = go.Figure(
    data=[
        go.Scatter(
            x=second_last_day_data.index,
            y=second_last_day_data.ta.rsi(
                close=second_last_day_data[("Close", ticker)]
            ),
            mode="lines",
        )
    ],
    layout=go.Layout(height=300),
)
rsi_fig.update_yaxes(range=[0, 100])
rsi_fig.add_hline(y=70, line_color="white")
rsi_fig.add_hline(y=30, line_color="white")


# Create the macd graph, plotting the macd and signal line. And also altering the height to 300
macd_fig = go.Figure(layout=go.Layout(height=300))
macd_fig.add_trace(
    go.Scatter(
        x=five_day_data.index,
        y=five_day_data.ta.macd(close=five_day_data[("Close", ticker)])["MACD_12_26_9"],
        mode="lines",
        name="MACD Line",
    )
)
macd_fig.add_trace(
    go.Scatter(
        x=five_day_data.index,
        y=five_day_data.ta.macd(close=five_day_data[("Close", ticker)])[
            "MACDs_12_26_9"
        ],
        mode="lines",
        name="Signal Line",
    )
)

# If the checkbox for bollinger is ticked, then display the bollinger.
# The bollinger is directly on the candlestick, therefore we do initial_candle_fig.add_trace().
# initial_candle_fig is the first graph they see before choosing their option
if show_bollinger:
    initial_candle_fig.add_trace(
        go.Scatter(
            x=second_last_day_data.index,
            y=second_last_day_data.ta.bbands(
                close=second_last_day_data["Close", ticker]
            )["BBL_5_2.0_2.0"],
            name="Lower",
        )
    )
    initial_candle_fig.add_trace(
        go.Scatter(
            x=second_last_day_data.index,
            y=second_last_day_data.ta.bbands(
                close=second_last_day_data["Close", ticker]
            )["BBU_5_2.0_2.0"],
            name="Upper",
        )
    )
    initial_candle_fig.add_trace(
        go.Scatter(
            x=second_last_day_data.index,
            y=second_last_day_data.ta.bbands(
                close=second_last_day_data["Close", ticker]
            )["BBM_5_2.0_2.0"],
            name="Middle",
        )
    )
rangebreaks = [dict(bounds=["sat", "mon"]), dict(bounds=[16, 9.5], pattern="hour")]

# The rangebreaks is to deal with blanks in time, because the market is not open 24/7.
# To ensure the graph is smooth, we deal with the gaps by removing them
initial_candle_fig.update_xaxes(rangebreaks=rangebreaks)
rsi_fig.update_xaxes(rangebreaks=rangebreaks)
macd_fig.update_xaxes(rangebreaks=rangebreaks)

# Example: Signal labeling exercise
st.write("### Signal Labeling Exercise")
st.write(
    "Look at the chart and label whether the signal is bullish, bearish, or neutral based on the indicators you toggled."
)
st.write("### Candlestick Chart")
st.plotly_chart(initial_candle_fig)

# This plots the rsi and macd graphs created earlier if the checkboxes are chosen
if show_rsi:
    st.write("### RSI")
    st.plotly_chart(rsi_fig)
if show_macd:
    st.write("### MACD")
    st.plotly_chart(macd_fig)


# Quiz section in the module
signal_options = ["Bullish", "Bearish"]
st.session_state["signal choice"] = st.radio("Your Signal Choice:", signal_options)
signal_choice = st.session_state["signal choice"]
st.write(f"You selected: **{signal_choice}**")
signal_confirm = st.button("Confirm Choice")

# Once the user choose bullish or bearish, we compare the second last day close price, to latest close price
if signal_confirm:
    latest_close = five_day_data[("Close", ticker)].iloc[-1]
    second_last_day_close = second_last_day_data[("Close", ticker)].iloc[-1]
    if (
        signal_choice == "Bullish" and latest_close > second_last_day_close
    ):  # If user chooses bullish (price goes up), and the price goes up, they are correct
        st.success("Good job, you identified the trend correctly")
    elif (
        signal_choice == "Bearish" and latest_close < second_last_day_close
    ):  # If user chooses bearish (price goes down), and the price goes down, they are correct
        st.success("Good job, you identified the trend correctly")
    else:  # If they are both chose the wrong option, they will get feedback they are wrong
        st.error(
            "Aw man, you got it wrong. But don't fret, wrong signals are very common in real life trading"
        )

    # This displays the candlestick graph after the user chose
    # This allows them to see what happened to the price after the snapshot that they saw
    feedback_candle_fig = go.Figure(
        data=[
            go.Candlestick(
                x=five_day_data.index,
                open=five_day_data[("Open", ticker)],
                high=five_day_data[("High", ticker)],
                low=five_day_data[("Low", ticker)],
                close=five_day_data[("Close", ticker)],
                name="Candles",
            )
        ]
    )

    # These two traces shows on the candlestick graph the 4 day close price they saw, and where it closed on the latest price
    feedback_candle_fig.add_trace(
        go.Scatter(
            x=[second_last_day_data.index[-1]],
            y=[second_last_day_close],
            mode="markers",
            marker=dict(color="green", size=10),
            name="4-Day Close",
        )
    )

    feedback_candle_fig.add_trace(
        go.Scatter(
            x=[five_day_data.index[-1]],
            y=[latest_close],
            mode="markers",
            marker=dict(color="red", size=10),
            name="Latest Close",
        )
    )
    feedback_candle_fig.update_xaxes(rangebreaks=rangebreaks)
    # Plots the graph
    st.plotly_chart(feedback_candle_fig)
    st.write("Click refresh to move on to the next chart")

# When the user clicks refresh, the ticker is updated, and the file is rerun so the new initial_candlestick_graph changes to reflect the new ticker
continuity = st.button("Refresh")
if continuity:
    st.session_state["ticker"] = random.choice(tickers)
    st.rerun()
st.divider()
