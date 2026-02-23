import streamlit as st

##################
# Title and Header#
##################
st.title("Let's learn Trading!")


st.divider()
st.subheader(
    "For all interactive questions, do check with our AI whether your prediction is correct."
)

st.header("""
Article 1: Introduction to Trading
""")


##########################
# Part 1 - Terminologies #
##########################
st.subheader("Terminologies")
st.write(
    "Before we dive into trading, it's important to differentiate between these 3 terminolgies that are often confused by many beginners:"
)
choices1 = [
    "Being thrifty",
    "Allocating money for future use",
    "Investing a lot of money in the bank for profit",
]
st.badge("Saving", color="blue")
st.selectbox("What is the definition", options=choices1)
st.badge("Trading", color="green")
st.radio(
    "What does it involve?",
    [
        "Buying an object at discount",
        "Buying something at lower price and selling at higher price",
        "Exchanging assets with others",
    ],
)
st.badge("Investment", color="red")
st.multiselect(
    "How is it different from trading",
    [
        "The time duration is longer",
        "It is specifically for companies",
        "It is only for physical and tangible objects",
    ],
)


st.space()
st.divider()

#########################
# Part 2 - Why Trading? #
#########################
st.subheader("Why do people trade?")
st.write("Based on statistics there are 3 reasons")
indiv, busi, govt = st.tabs(["Individuals", "Businesses", "Government"])

indiv.metric("Education", "40%", "Expose to various markets")
indiv.metric("Profit", "5%", "Make a living out of it")
indiv.metric("Entertainment", "10%", "Find satisfaction and as a recreation")

busi.image("https://www.fpmarkets.com/assets/images/blogs/risk.png")
busi.image(
    "https://cdn.educba.com/academy/wp-content/uploads/2024/03/Essay-on-Competition.jpg"
)
busi.image(
    "https://thumbs.dreamstime.com/b/reputation-icon-monochrome-simple-community-templates-web-design-infographics-line-element-symbol-246513236.jpg"
)


govt.write("Obtain Profits so that they can privde people with resources")
govt.write("Not only that, it creates trust and support of the government with people")
govt.write("Help other countries with funding for emergencies using these profits")


st.space()
st.divider()

#################################
# Part 3 - Trading vs Investment#
#################################
st.subheader("The relationship between inflation and trading")
time, risk = st.columns(2, gap="medium")
time.badge("Time Horizon", color="blue")
time.image("https://tfagroup.co.uk/wp-content/uploads/2022/04/time-horizonsgold.jpg")
time.write(
    "Investing is a Long Term Horizon where wealth is accumulated over a long period of time in years or decades. Whereas Trading is a Short Term Horizon where assets are bought and sold within a short period of time such as days, weeks or months."
)
risk.badge("Risk Volatility", color="red")
risk.image(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSieBS8c-jXHuCxX8bYc2WKRycYE165fKFvQ&s"
)
risk.write(
    "The risks involved in investing is lower as the timeframe is longer to recover from losses. People exploit this volatility to earn high quickly while risking their earnings if prices fall. Whereas investing is more reliable as it does not cause significant losses even if the market falls due to the accumulated wealth."
)

st.space()
st.divider()

############################
# Part 4 - Financial Markets#
############################
st.subheader("Financial Markets (Choose the market which best matches the description)")

lst = ["Exchange Traded Funds (ETF)", "Foreign-Exhange (Forex)", "Cryptocurrencies"]
st.segmented_control(
    "Basket of multiple assets, providing flexibility and convenience while Trading. Reduce company-specific risks.",
    lst,
)
st.badge(
    "Some examples include government bonds, commodities like gold and even other countries' currencies.",
    color="blue",
)
st.space()
st.segmented_control(
    "A global marketplace for exchanging currencies. It allows multiple stakeholders from individuals to businesses to convert their money for international trade.",
    lst,
)
st.badge(
    "Do note that unlike other markets, they are highly volatile due to changing geopolitics and economy of countries.",
    color="green",
)
st.badge("Commonly exchanged currencies are USD, EUR, JPY and GBP?", color="green")
st.space()
st.segmented_control(
    "Decentralised system where the autonomy of the markets are not controlled by commercial banks and government.",
    lst,
)
st.badge(
    "It uses blockchain technology which digitally tracks and monitors online transactions",
    color="violet",
)
st.badge(
    "The famous type is Bitcoin which is the 1st system used since 2009", color="violet"
)

st.space()
st.divider()

######################
# Part 5 - Order Types#
######################
st.subheader("Orders")
st.write(
    "An Order is a specific set of instruction given by a broker or trader to trade an asset under specific conditions. For basics we will be looking at 2 main types of orders in trading."
)
st.badge("Market Order", color="violet")
st.write(
    "Market Orders are used when there is high liquidity of markets. This would mean that people who are trading will need to think and buy decisively within a short period of time."
)
st.badge("Limit Orders", color="orange")
st.write(
    "Limit Orders are instructions given to a broker to sell or buy a security at a specific order or higher. Unlike Market Order where decisions have to be made quickly, Limit Orders require careful observation of the market."
)
st.write(
    "When the price is below market price, an asset will be bought. Similary, when the market price increases, orders will be given to sell the asset to ensure maximum profit is gained."
)
st.write(
    "If the market price does not reach the desired or expected price, the order is said to be unfilled."
)

st.space()
st.divider()

##########################
# Part 6 - Risk Management#
##########################
st.subheader("Risk Management")
st.subheader("Choose the description which you feel is correct")

st.badge("1)Emotional Discipline", color="green")
with st.popover("Select the definition"):
    x = st.radio(
        "Choose",
        [
            "Constant Fear of losing money",
            "Being overconfident of making profits",
            "Making decisions with structure and not emotions",
        ],
    )
st.write(x)
st.space()
st.badge("2)Lack of Knowledge ", color="red")
with st.popover("What is NOT a possible factor?"):
    x = st.pills(
        "Consequences",
        [
            "Following other traders blindly",
            "Underestimating liquidity of market value",
            "Being exposed to various courses on trading",
        ],
    )
st.write(x)
st.space()
st.badge("*3)Taxes on Profits", color="yellow")
st.write("Trading excessively increases taxes and brokerage fees which impact profits.")

st.space()
st.divider()

##############################
# Part 7 - Risk Factor Profits#
##############################
st.subheader("Mathematical Calculation of Risk Factors in Trading")

with st.popover("Calculate Risk-Reward Ratio"):
    st.badge("Step 1: Entry Price - Stop-Loss Price", color="yellow")
    st.markdown("This is the maximum amaount you are willing to lose")
    st.space()
    st.badge("Step 2: Take-Profit Price - Entry Price", color="yellow")
    st.markdown("This is the target profit you are willing to make")
    st.space()
    st.badge("Divide the 1st value by 2nd value", color="yellow")
    st.markdown("If the ratio is more than 1, the chances are more favourable to you.")
st.write("Stop-loss Take-Profit Ratio is also known as Risk-Reward Ratio.")
st.write(
    "Stop loss is desined to protect a trader's capital in case the market moves against them. It does so by automatically exiting the position in market, thus reducing potential losses."
)
st.write(
    "Take-Profit locks in the profits gained by a particular margin. It caps the profits earned to reduce greed which can lead to reversal potential losses."
)
st.write(
    "It strengthens the discpline of traders by ensuring they trade passively without the need to monitor the markets. On top of that, it helps them to not make impulsive decisions."
)
