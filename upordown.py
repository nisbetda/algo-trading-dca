import pprint
import urllib
import time
import json
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
from td.client import TDClient
from config import CLIENT_ID, REDIRECT_URI, JSON_PATH, ACCOUNT_NUMBER_OG, ACCOUNT_NUMBER_IRA, ACCOUNT_NUMBER
from stock_list import stock_list

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

# function , using a loop, to find the MA for a given symbol
def getmovingaverage(list):
  print("A moving average function") 

  for s in stock_list:
    symbol = s
    pprint.pprint("-------" +symbol+ "---------------" )

    # Moving Average calculations
    month_price = td_client.get_price_history(
      symbol, 
      period_type= 'month', 
      period= 1, 
      frequency_type= 'daily', 
      frequency= 1, 
      extended_hours=True
    )
    year_price = td_client.get_price_history(
      symbol, 
      period_type= 'year', 
      period= 1, 
      frequency_type= 'daily', 
      frequency= 1, 
      extended_hours=True
    )

    #MA calculations 
    candle_month = month_price["candles"]
    candle_year = year_price["candles"]

    sum_month = 0
    sum_year = 0
    for close in range(len(candle_month)):
      sum_month += candle_month[close]["close"]

    for close in range(len(candle_year)):
      sum_year += candle_year[close]["close"]
      
    print("23DayMA: ", sum_month/23)
    print("253DayMA: ", sum_year/253)

  

  


#call the function
getmovingaverage(stock_list)
pprint.pprint("-----------------------bye-------------------------")