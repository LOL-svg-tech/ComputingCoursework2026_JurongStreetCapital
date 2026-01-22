import streamlit as st


##################
#Title and Header#
##################
st.title("Let's learn Trade!")


st.markdown("This app is designed to help youths are very new to trading to get them started on these good financial habits.")
st.markdown("This package is specifically designed for those who have very little knowledge of trading")
st.markdown("This package entails 5 articles starting with foundation and ending with Quantitative Trading. After each article, you will have to complete a quiz in order to progress to the next article.")


st.divider()


#############
# Module 1 #
#############
st.header(
'''
Article 1:  Introduction to Trading
''')
# Part 1 - Terminologies #
st.subheader("Terminologies")
st.write("Before we dive into trading, it's important to differentiate between these 3 terminolgies that are often confused by many beginners:")
col1, col2, col3  = st.columns(3)
col1.badge("Saving", color = "blue")
col1.write("It is the act of allocating money for future use, rather than spending it immediately.")
col2.badge("Trading", color = "green")
col2.write("It is the act of buying and selling assets (something you own) with the hope of getting a profit. For example, let's take a retail item such as a bicycle. Let's say a person buys a bicycle for 100 SGD. He then finds his friend who wants the same bicycle. He sells this bicycle for 120 SGD. Now he has traded a bicycle for 20 SGD profit")
col3.badge("Investment", color = "red")
col3.write("It is essentially similar to trading but with a longer timeframe. It involves buying assests with a hope of getting profit in the future such as company's shares, bonds and stocks. You can learn this in deatil at the investing tab.")


st.space()


# Part 2 - Why Trading? #
st.subheader("Why do people trade?")
st.write("In the financial world, 3 main parties involve in trading:")
indiv, busi, govt = st.tabs(["Individuals", "Businesses", "Government"])


indiv.write("Individuals trade for a variety of reason ranging from eductional purposes to making profits to run their households. ")
indiv.write("For Education: Individuals can learn about the trading market by analysing the general trends, predicting the right time to sell their assets. They may do it gain early exposure before moving on to bigger markets and assets that hold more value. ")
indiv.write("For income: They may do it a business hoping to make side profits that can be accumulated over the years as well as to increase their overall net worth. ")
indiv.write("For entertainment: Some even trade for entertainment, as they feel joy and satisfied in knowing that their market value predictions were right")


busi.write("There are infact many reasons why businesses trade. However, for the sake of simplicity, let's use these 4 reasons to build up our knowledge, later on")
busi.write("Reducing potential risks: Businesses trade to grow revenue (money earn by selling goods). Businesses especially Small and Medium Enterprises (SMEs) have employees to trade assests such as stock to get profit so that in the event that their main business flops, they can use these profit to survive. ")
busi.write("Competition: They can increase their net worth and stay ahead of competition by driving through innovation and buying new goods.")
busi.write("Reputation: To build reputation and image for their brands and products.")
busi.write("Disposal of goods: When businesses manufacture more than what they typially sell and do not have the capacity to store them, they might trade to distribute these goods taht are in surplus")


govt.write("The main reason behind why governments trade is to gain profit so that they can improve the quality of infrastructure and facilities for their people so as to improve their quality of life.")
govt.write("In countries like Singapore whee natural resources are scarce, trading can provide profits to gain access to these resources that tehy can use to improve their country. ")
govt.write("With more profits for the government, it can also lead to decline in consumer taxes for the people, cost of living which is beneficial for the people.")
govt.write("Not only that, it creates trust and support wihin the government and the companies as both are contributing to the economy. And these profits if given to other countries as funds or support can create political and regional stability.")



st.space()


# Part 3 - Trading vs Investment
st.subheader("The relationship between inflation and trading")
time, risk = st.columns(2, gap = "medium")
time.badge("Time Horizon", color = "blue")
time.write("Investing is a Long Term Horizon where wealth is accumulated over a long period of time in years or decades. Whereas Trading is a Short Term Horizon where assets are bought and sold within a short period of time such as days, weeks or months.")
risk.badge("Risk Volatility", color = "red")
risk.write("The risks involved in investing is lower as the timeframe is longer to recover from losses. People exploit this volatility to earn high quickly while risking their earnings if prices fall. Whereas investing is more reliable as it does not cause significant losses even if the market falls due to the accumulated wealth.")

#Part 4 - Financial Markets
st.subheader("Financial Markets")
etf, forex, crypto = st.tabs(["ETFs", "Forex", "Cryptocurrency"])
etf.write("ETFs or Exchange Traded Funds is a basket of multiple assets, providing flexibility and convenience while Trading. They reduce company-specific risks.They can be traded even on days when markets fluctuate which can't be done with mutual assets")
etf.write("Some examples include government bonds, commodities like gold and even other countries' currencies.")
forex.write("Forex or Foreign-Exhange is a global marketplace for exchanging currencies. It allows multiple stakeholders from individuals to businesses to convert their money for international trade.")
forex.write("Do note that unlike other markets, forex markets are highly volatile due to changing geopolitics and economic situations of various countries.")
forex.write("Fun Fact: Do you know that the commonly exchanged currencies are USD, EUR, JPY and GBP?")
crypto.write("Cryptocurrencies is a decentralised system where the autonomy of the markets are not controlled by commercial banks and government.")
crypto.write("It used blockchain technology which digitally tracks and monitors online transactions and are operated digitally with no physical means.")
crypto.write("The famous type of cryptocurrency is Bitcoin which is the 1st system used since 2009 which has the highest value and is highly recognised.")

#Part 5 - Order Types
st.subheader("Orders")
st.write("An Order is a specific set of instruction given by a broker or trader to trade an asset under specific conditions. For basics we will be looking at 2 main types of orders in trading.")
st.badge("Market Order", color = "violet")
st.write("Market Orders are used when there is high liquidity of markets. This would mean that people who are trading will need to think and buy decisively within a short period of time.")
st.badge("Limit Orders", color = "orange")
st.write("Limit Orders are instructions given to a broker to sell or buy a security at a specific order or higher. Unlike Market Order where decisions have to be made quickly, Limit Orders require careful observation of the market.")
st.write("When the price is below market price, an asset will be bought. Similary, when the market price increases, orders will be given to sell the asset to ensure maximum profit is gained.")
st.write("If the market price does not reach the desired or expected price, the order is said to be unfilled.")

#Part 6 - Risk Management
st.subheader("Risk Management")
st.write("Why do most traders lose money despite being careful with their decisions?")

