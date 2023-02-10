
from urllib.request import urlopen, Request
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

def trading_execution_buy(orderqty, ticker):
    stock_client = StockHistoricalDataClient("PK7U67M8TOGVP8HD8EJW",  "jyLQlseSgUhbE7sc32CDFCERNbfjyEZh0gcisa43")
    multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["AAPL"])
    latest_multisymbol_quotes = stock_client.get_stock_latest_quote(multisymbol_request_params)
    spy_latest_ask_price = latest_multisymbol_quotes["AAPL"].ask_price
    trading_client = TradingClient('PK7U67M8TOGVP8HD8EJW', 'jyLQlseSgUhbE7sc32CDFCERNbfjyEZh0gcisa43', paper=True)
    market_order_data = MarketOrderRequest(
            symbol=ticker,
            qty=orderqty,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
            )
    market_order = trading_client.submit_order(
        order_data=market_order_data
        )
    return market_order_data

def trading_execution_sell(orderqty, ticker):
    stock_client = StockHistoricalDataClient("PK7U67M8TOGVP8HD8EJW",  "jyLQlseSgUhbE7sc32CDFCERNbfjyEZh0gcisa43")
    multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["AAPL"])
    latest_multisymbol_quotes = stock_client.get_stock_latest_quote(multisymbol_request_params)
    spy_latest_ask_price = latest_multisymbol_quotes["AAPL"].ask_price
    trading_client = TradingClient('PK7U67M8TOGVP8HD8EJW', 'jyLQlseSgUhbE7sc32CDFCERNbfjyEZh0gcisa43', paper=True)
    market_order_data = MarketOrderRequest(
            symbol=ticker,
            qty=orderqty,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY
            )
    market_order = trading_client.submit_order(
    order_data=market_order_data
    )

    return market_order_data
def generate_trade(prompt):
    emp_str = ""
    if "buy" in prompt.lower():
        if "shares" in prompt.lower():
            if "apple" in prompt.lower():
                for digits in prompt:
                    if digits.isdigit():
                        emp_str = emp_str + digits
                if emp_str > "0":
                    message = "Ok I have created order to buy " + emp_str + " stocks of Apple" + "\n Here are the order details:" + str(trading_execution_buy(emp_str, "AAPL"))
                else:message = "how many Apple stocks would you like to buy?"
    if "sell" in prompt.lower():
        if "shares" in prompt.lower():
            if "apple" in prompt.lower():
                for digits in prompt:
                    if digits.isdigit():
                        emp_str = emp_str + digits
                if emp_str > "0":
                    message = "I have created order to sell " + emp_str + " shares of Apple stock." + "\n Here are the order details:" + str(trading_execution_sell(emp_str, "AAPL"))
                else:message = "how many Apple stocks would you like to sell?"
    if "buy" in prompt.lower():
        if "shares" in prompt.lower():
            if "connocophilips" in prompt.lower():
                for digits in prompt:
                    if digits.isdigit():
                        emp_str = emp_str + digits
                if emp_str > "0":
                    message = "I have created order to buy " + emp_str + " shares of Connocophilips stock" + "\n Here are the order details:" + str(trading_execution_buy(emp_str, "COP"))
                else:message = "how many Connocophilips stocks would you like to buy?"
    if "sell" in prompt.lower():
        if "shares" in prompt.lower():
            if "connocophilips" in prompt.lower():
                for digits in prompt:
                    if digits.isdigit():
                        emp_str = emp_str + digits
                if emp_str > "0":
                    message = "I have created order to sell " + emp_str + " shares of Connocophilips stock" + "\n Here are the order details:" + str(trading_execution_sell(emp_str, "COP"))
                else:message = "how many Connocophilips stocks would you like to sell?"
    #else: message = "I didn't catch your prompt! Please try again"

    return message