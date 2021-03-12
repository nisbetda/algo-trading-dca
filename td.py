#import urllib
#import json
import requests
import pprint
#import dateutil.parser
#from datetime import datetime
from config import CLIENT_ID

#prices
endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('GOOG')

#payload
payload = {'apikey':CLIENT_ID,
            'periodType':'day',
            'frequencyType':'minute',
            'frequency':'1',
            'period':'2',
            'endDate':'1615415146000',
            'startDate':'1615415563',
            'needExtendedHoursData':'true'}

#make request
content = requests.get(url= endpoint, params= payload)

#convert to dictionary
data = content.json()
pprint.pprint(data)


#----------------------------
#quote 
endpoint_2 = r"https://api.tdameritrade.com/v1/marketdata/{}/quotes".format('GME')

#payload
payload_2 = {'apikey':CLIENT_ID}

#make request
content = requests.get(url= endpoint_2, params= payload_2)

#convert to dictionary
data_2 = content.json()
pprint.pprint('===========')
pprint.pprint(data_2)


