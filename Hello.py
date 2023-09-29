# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import yfinance as yf
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    # https://www.markdownguide.org/cheat-sheet/
    st.write("""
    ### Simple Stock Price App
    
    Shown are the stock **closing price** and ***volume*** of Google!
    
    """)
    
    # https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
    #define the ticker symbol
    tickerSymbol = 'GOOGL'
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    
    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)

if __name__ == "__main__":
    run()
