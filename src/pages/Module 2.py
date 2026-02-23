import streamlit as st

st.title("Let's learn Trading!")

st.divider()
# divider for divider

st.header("Article 2: Technical Analysis Foundations")
st.subheader(
    "When we say technical indicators, we mean using numbers which can help us make an informed decision"
)
# Subheader for titles of chapters
st.subheader("Candlestick charts")
st.markdown("""
Candlesticks or also refered to as **OHLC** is a mean of plotting the **Open**, **High**, **Low** and **Close** price of an instrument for a certain timeframe. (E.g. a 5min candle, meaning that the candle will be the Open, High, Low, Close prices of an instrument for a specific 5 minute period)
            
""")
st.image(
    "https://cdn.britannica.com/13/237813-050-0CA3E424/candlestick-chart-definition.jpg"
)
st.markdown(
    "As you can see, the range between the open and the close forms the body, whilst the range from the high/close to the open/low forms the 'wick' of the candle, this is why we call such datapoints in a chart candlesticks"
)

st.subheader("Meanings of the different prices:")
# Using markdown so i can bold things
st.markdown("""
The **Open** Price:

- It refers to the opening price traded of an instrument during its candle's timeframe.
- When the NYSE opens at 9:30 AM, the first price at which people are trading the instrument will be the opening price
        
The **High** Price:
            
- It refers to the highest price traded at one point during the candle's timeframe
- In a fifteen minute candle, at one point the instrument traded at $500, the highest price traded, this will be the high

The **Low** Price:  
- Just like the High price, it is simply the lowest price of an instrument traded during a candle's timeframe

The **Close Price**:
- Just like the Open price, the Close price will be the last price traded of an instrument during a candle's timeframe
- When the NYSE closes at 4:00 AM, the price traded at that time will be the close price as the market closes                   
""")

st.subheader("Determining bearish/bullish candles")
st.write(
    "If the close price is higher than the opening price, this means it is a bullish (typically green) candle, while if the close price is less than that of the opening, it will be a bearish (typically red candle)"
)

st.subheader("Determining market structure")
up, down, range = st.tabs(["Uptrend", "Downtrend", "Ranges"])


range.write(
    "The range of a symbol, it is a mouthful of words, but it is defined as the the Highest Price - Lowest Price within a certain timeframe"
)
range.write(
    "We can use the range to determine thing ssuch as Volatility, if there is a higher range, prices have more space to jump around, and this means that it is more volatile."
)
range.write("We can also use ranges to determine the support/resistance levels")
range.image(
    "https://www.investopedia.com/thmb/kqBSGb0bXZ0mXqZ315yoGMg-xP0=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/dotdash_Final_Support_and_Resistance_Basics_Aug_2020-01-1c737e0debbe49a88d79388977f33b0c.jpg"
)
range.write(
    "In this example, notice how the top of the range acts as a 'resistance' level where price cannot break through. The inverse applies as shown below"
)
range.image(
    "https://www.investopedia.com/thmb/y7FneUCq0_elrB_K7f-1ToBYBGk=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/dotdash_Final_Support_and_Resistance_Basics_Aug_2020-02-fc5a37801b9944a6bc17886b19c3ea14.jpg"
)
up.write(
    "In an uptrend, prices are usually following a structure of Higher Highs, and Higher Lows"
)
up.image("https://www.binaryoptions.com/wp-content/uploads/Uptrend-trendline-FTSE-100-Index-Chart.png")
up.write("Image provided by binaryoptions.com")
down.write(
    "In an downtrend, prices are usually following a structure of Lower Highs, and Lower Lows"
)
down.image("https://www.binaryoptions.com/wp-content/uploads/downtrend-with-lower-lows-and-lower-highs.png")
down.write("Image provided by binaryoptions.com")

# Add images and descriptions with tabs

st.subheader("Chart Timeframes and Bias")
st.markdown("In trading charts, there are multiple timeframes available, and using **higher/lower** timeframes can be used to determine existing market bias")
st.markdown("**Market Bias**: It is the market's overall direction or inclination towards a specific direction either when prices go up or down. It can be obtained through using different timeframes and technical analysis")
st.markdown("A **Higher** timeframe: this is defined as a when a candle represents a longer period")
st.markdown("A **Lower** timeframe: this is defined as when a candle represents a shorter period")
st.markdown("""Here are some common combinations for different types of traders: 
            
- Day Traders(People who trade within a single day), **Daily(1d)** for market direction(Longer term trends) + **(1H/30min)** for structure(Think about shorter term market trends) and **(15min/5m)** for entries(When you buy and sell)
- Swing Traders(People who aren't as active as day traders and trade within the week), **Weekly(1W)** for market direction + **(1d)** for structure) and **(4h/1h)** for entries
            
We can use the stacking of timeframes to avoid losing to much more stronger, longer-timeframe market movements during trading, and most importantly identify the market context which are the  trend and Support and Resistance (SR) levels. And when searching for entries(best prices to enter a position) we use Lower Timeframes combined with Technical Analysis to buy at the best price. This is especially important for more active traders, as some times a difference of a few dollars in the stock price can mean earning or losing for the day!
""")

