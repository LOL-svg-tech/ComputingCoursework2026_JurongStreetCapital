import streamlit as st


##################
#Title and Header#
##################
st.title("Let's learn Trade!")


st.markdown("This app is designed to help youths are very new to trading to get them started on these good financial habits.")
st.markdown("This course is specifically designed for those who have very little knowledge of trading")
st.markdown("This course entails 15 modules starting with foundation and ending with ethics. After each module, you will have to complete a quiz in order to progress to the next module.")


st.divider()


#############
# Module 1 #
#############
st.header(
'''
Module 1:  Introduction to Trading
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


# Part 3 - Inflation and Trading
st.subheader("The relationship between inflation and trading")
