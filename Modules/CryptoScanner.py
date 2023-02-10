import os
from urllib.request import urlopen, Request
import pandas as pd
import requests
import json

#CoinGecko API funtion 
def CoinGecko(coin):
    if coin == "bitcoin":
        bob = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", headers= {"accept": "application/json"})
        price = bob.json()['bitcoin']["usd"]
    elif coin == "ethereum":
        bob = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd", headers= {"accept": "application/json"})
        price = bob.json()['ethereum']["usd"]
    elif coin == "holdbitcoin":
        bob=  requests.get("https://api.coingecko.com/api/v3/companies/public_treasury/bitcoin", headers={"accept": "application/json"})
        price = ""
        for i in range(3):
            price = price + str(bob.json()['companies'][i])
        price = price[10:27] + " with total holding of" + price[90:97] + " BTC" + " Total current value in USD" + price[123:134] + " holds the most bitcoins."
    return price 
#string manipulation for user interaction for crypto scanner 
def crypto_query(prompt):
    if "price" in prompt.lower():
        if "bitcoin" in prompt.lower():
                    message = "Price of bitcoin is " + str(CoinGecko("bitcoin"))
    if "price" in prompt.lower():
        if "ether" in prompt.lower():
                message = "Price of ether " + str(CoinGecko("ethereum"))
    if "holds" in prompt.lower():
         if "bitcoin" in prompt.lower():
              message = str(CoinGecko("holdbitcoin"))
    return message