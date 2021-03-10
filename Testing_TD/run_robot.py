import time as true_time
import pprint
import pathlib
import operator
import pandas as pd

from datetime import datetime
from datetime import timedelta
from config import CLIENT_ID , REDIRECT_URI, JSON_PATH, ACCOUNT_NUMBER
 
from robot import PyRobot
from indicators import Indicators



# Initalize the robot.
trading_robot = PyRobot(
    client_id=CLIENT_ID,
    redirect_uri=REDIRECT_URI,
    credentials_path=JSON_PATH,
    trading_account=ACCOUNT_NUMBER
    #paper_trading=False
)

# Create a Portfolio
trading_robot_portfolio = trading_robot.create_portfolio()
# pprint.pprint(trading_robot_portfolio)
# Define mutliple positions to add.
multi_position = [
    {
        'asset_type': 'equity',
        'quantity': 2,
        'purchase_price': 4.00,
        'symbol': 'TSLA',
        'purchase_date': '2020-01-31'
    },
    {
        'asset_type': 'equity',
        'quantity': 2,
        'purchase_price': 4.00,
        'symbol': 'SQ',
        'purchase_date': '2020-01-31'
    }
]

# Grab the New positions
new_positions = trading_robot.portfolio.add_positions(positions=multi_position)

trading_robot_portfolio.add_position(
    symbol='MSFT',
    quantity=10,
    purchase_price=10,
    asset_type='equity',
    purchase_date='2020-04-01'
)

pprint.pprint(trading_robot.portfolio.positions)
# If the Market is open, print some quotes.
if trading_robot.regular_market_open:
    pprint.pprint('Regular Market Open')

# If the Post Market is Open, do something.
elif trading_robot.post_market_open:
    pprint.pprint('Post Market Open')

# If the Pre Market is Open, do something.
elif trading_robot.pre_market_open:
    pprint.pprint('Pre Market Open')

#Get the current quotes
current_quotes = trading_robot.grab_current_quotes()
pprint.pprint(current_quotes)

# Grab historical prices, first define the start date and end date.
 
 # Create a new Trade Object.
new_trade = trading_robot.create_trade(
    trade_id='long_msft',
    enter_or_exit='enter',
    long_or_short='short',
    order_type='lmt',
    price=1.00
)

# Make it Good Till Cancel.
new_trade.good_till_cancel(cancel_time=datetime.now())

# Change the session
new_trade.modify_session(session='am')

# Add an Order Leg.
new_trade.instrument(
    symbol='MSFT',
    quantity=2,
    asset_type='EQUITY'
)

# Add a Stop Loss Order with the Main Order.
new_trade.add_stop_loss(
    stop_size=.10,
    percentage=False
)

# Print out the order.
pprint.pprint(new_trade.order)

