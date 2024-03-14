import streamlit as st
import yfinance as yf
import pandas as pd

# Create a sidebar for user input
st.sidebar.header("Input Stock Symbol")
tickerSymbol = st.sidebar.text_input("Enter Ticker Symbol", "GOOGL")  # Default value

# Get stock data based on user input
try:
  tickerData = yf.Ticker(tickerSymbol)
  tickerDf = tickerData.history(period='Id', start='2010-05-11', end='2024-02-29')
except:
  st.error(f"Error: Could not retrieve data for '{tickerSymbol}'. Please check the symbol and try again.")
  tickerDf = pd.DataFrame()  # Create an empty DataFrame in case of error

# Display the data if successfully retrieved
if not tickerDf.empty:
  st.write("""
  # Simple Stock Price App

  Shown are Stocks **Closing Price** and **Opening Volumes** for: **{tickerSymbol}**
  """)

  st.line_chart(tickerDf.Close)
  st.line_chart(tickerDf.Volume)
