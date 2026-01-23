import streamlit as st

st.title("Let's learn Trade!")

st.divider()

st.header("Article 3: Indicator-Based Trading")

st.subheader("Indicators are not magic. Past performance does not guarantee future results.")
st.subheader("Indicators vs Reality: What do they actually do?")
st.write("Indicators apply math to historical market data in order for traders to understand what is going on.")
st.markdown("""
Indicators are based on **past data**, which means:
- They **summarize historical prices**.
- They can indicate **volatility or momentum**.
- They are inherently **lagging**, not predictive.
""")
st.write("This means that indicators should be used as tools, and not as prophecies.")

st.divider()
st.subheader("Different Types of Indicators")

rsi, macd, bollinger = st.tabs(["Relative Strength Index", "Moving Average Convergence Divergence", "Bollinger Bands"])

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
- **Indicator stacking:** Using too many indicators can create confusion, not clarity.
- **Late entries:** Waiting for all indicators to confirm often means entering after most of the move is over.
- **Over-optimization:** Adjusting indicator parameters too closely to past data reduces future reliability.
- **Setting take profits and stop losses incorrectly**
    - Take Profit too far → price may never reach it; Take Profit too close → miss potential gains.
    - Stop Loss too far → risk larger losses; Stop Loss too close → risk being stopped out on a temporary dip.
""")

st.divider()
st.subheader("Interactive Indicator Learning")

st.write("You can experiment with indicators on charts and practice identifying signals.")

# Example: Toggle indicators on a sample chart
show_rsi = st.checkbox("Show RSI")
show_macd = st.checkbox("Show MACD")
show_bollinger = st.checkbox("Show Bollinger Bands")

st.write("*(Charts would appear here with selected indicators in a full app)*")

# Example: Signal labeling exercise
st.write("### Signal Labeling Exercise")
st.write("Look at the chart and label whether the signal is bullish, bearish, or neutral based on the indicators you toggled.")
signal_options = ["Bullish", "Bearish", "Neutral"]
signal_choice = st.radio("Your Signal Choice:", signal_options)
st.write(f"You selected: **{signal_choice}**")

st.divider()
st.write("### Mini Challenge")
st.write("Combine indicators to find a potential trade setup. Consider:")
st.markdown("""
- Momentum (RSI)
- Trend confirmation (MACD)
- Volatility (Bollinger Bands)
""")
st.write("Try to spot a confluence where all three indicators agree.")

st.success("Great! You've completed Module 3 on Indicator-Based Trading. 🎉")
