import pprint
from dalton import ACCOUNT_NUMBER
from td.client import TDClient


# from config.py
CONSUMER_KEY = 'RGAJLH1SSJARW9AZ8W70VIHC07WAXMGF'
REDIRECT_URI = 'https://localhost/'
JSON_PATH = '/Users/daltonnisbett/Documents/Testing_TD/td_state.json'

# Create new instance of the client
td_client = TDClient(
    client_id = CONSUMER_KEY, 
    redirect_uri = REDIRECT_URI, 
    credentials_path = JSON_PATH
)

# Login to a new session
# AFTER 90 DAYS THE AUTHENTICATION PROCESS NEEDS TO BE DONE AGAIN
# consists of:
# loging in with credentials at the link in the terminal
# then copying address from the web bar (ignore error from webpage) and pasting it in the terminal below
td_client.login()


#A Limit Order for FB @ $20.0
limit_order = {
    "orderType": "LIMIT",
    "session": "SEAMLESS",
    "duration": "DAY", 
  
    "price": 20.0,
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
      {
        "instruction": "BUY",
        "quantity": 1,
        "instrument": {
          "symbol": "FB",
          "assetType": "EQUITY"
        }
      }
    ]
}


# Place the order called "limit_order"
#new_order_response = td_client.place_order(account = ACCOUNT_NUMBER, order = limit_order)
# pprint.pprint(new_order_response)

# Get the positions from account
accounts = td_client.get_accounts(account = ACCOUNT_NUMBER, fields = ['positions'])
securitiesAccount = accounts["securitiesAccount"]
positions = securitiesAccount["positions"]

# for instrument in positions_2:
#   print(positions_2)
#   for i in instrument:
#     print(i[1])

#pprint.pprint(accounts)

for p in positions:
  print(p["instrument"]["symbol"])
  symbol = p["instrument"]["symbol"]
  quote = td_client.get_quotes(instruments = [symbol])
  for lp in quote:
    price = lp["lastPrice"]
    pprint.pprint(price)

  








