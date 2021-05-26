import pprint
import urllib
import time
import json
import requests
import pprint
from datetime import datetime
from datetime import timedelta
from td.client import TDClient
from config import CLIENT_ID, REDIRECT_URI, JSON_PATH, ACCOUNT_NUMBER_OG, ACCOUNT_NUMBER_IRA, ACCOUNT_NUMBER

# Create new instance of the client, using account data from config.py
td_client = TDClient(
    client_id = CLIENT_ID, 
    redirect_uri = REDIRECT_URI, 
    credentials_path = JSON_PATH
)

# Login to a new session
# AFTER 90 DAYS THE AUTHENTICATION PROCESS NEEDS TO BE DONE AGAIN
# consists of:
# loging in with credentials at the link in the terminal
# then copying address from the web bar (ignore error from webpage) and pasting it in the terminal below
td_client.login()

#Test buy order
#A Limit Order for AAPL @ $100.00
limit_order = {
    "orderType": "LIMIT",
    "session": "SEAMLESS",
    "duration": "DAY",
  
    "price": .50,
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
      {
        "instruction": "BUY",
        "quantity": 1,
        "instrument": {
          "symbol": "SPY",
          "assetType": "EQUITY"
        }
      }
    ]
}

# Place the order called "limit_order"
#new_order_response = td_client.place_order(account = ACCOUNT_NUMBER, order = limit_order)
#pprint.pprint(new_order_response)

# Get the positions from account
accounts = td_client.get_accounts(account = ACCOUNT_NUMBER, fields = ['positions'])
securitiesAccount = accounts["securitiesAccount"]
positions = securitiesAccount["positions"]

for p in positions:
  print(p["instrument"]["symbol"])
  symbol = p["instrument"]["symbol"]
  quote = td_client.get_quotes(instruments = [symbol])
  print(quote.get(symbol).get('52WkHigh'))
  #get current quote##########################################################################
  endpoint_2 = r"https://api.tdameritrade.com/v1/marketdata/{}/quotes".format(symbol)

  #payload
  payload_2 = {'apikey':CLIENT_ID}

  #make request
  content = requests.get(url= endpoint_2, params= payload_2)

  #convert to dictionary
  data_2 = content.json()

  net_change = data_2.get(symbol).get('regularMarketNetChange')
  bid_price = data_2.get(symbol).get('bidPrice')

  pprint.pprint("net change: {}".format(net_change))
  pprint.pprint("bid_price: {}".format(bid_price))
  #pprint.pprint('===========')
  #GET HISTORICAL PRICE
  endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(symbol)

  #payload
  #Grab historical prices
  payload = {'apikey':CLIENT_ID,
              'periodType':'year',
              'period': '1',
              'frequencyType':'monthly',
              'frequency':'1',
              'needExtendedHoursData':'true'}

  #make request
  content = requests.get(url= endpoint, params= payload)

  #convert to dictionary
  data = content.json()




      








