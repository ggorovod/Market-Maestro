#All imports
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import bcrypt
from streamlit_chat import message
import os
from dotenv import load_dotenv
import openai
from streamlit_option_menu import option_menu
from newsapi import NewsApiClient
from urllib.request import urlopen, Request
import pandas as pd
import nltk
#nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
from datetime import date
from datetime import timedelta
import requests
import json
#from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd
from alpaca.trading.client import TradingClient
from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.live import StockDataStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus
from alpaca.trading.stream import TradingStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import Trading
import Sentiment
import CryptoScanner
import OpenAI