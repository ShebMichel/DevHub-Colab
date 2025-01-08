# http://workshop.robin.com.au/chat/week3
import requests

response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale', headers={'user-agent': ''})

print(response.content)
print('Done ')
############
import feedparser
import requests

response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale', headers={'user-agent': ''})

feed1 = feedparser.parse(response.content)
print('parsing data to recreate a dictionary:')
print(feed1)
print('Done ')
####################
#When you print out feed1, it looks like a mess, but you can try importing pprint and print out feed1 in a more formatted way. You can also print out the type of feed as follows:
from pprint import pprint
print('looking at pprint: ')
pprint(feed1)
print('Done ')
##
print('Ways of importing: ')

import feedparser
import pprint

feed1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')

pprint.pprint(feed1)
print('Done ')

####
from feedparser import parse
from pprint import pprint

feed1 = parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')

pprint(feed1)
print('Done')
#####
import feedparser
import pprint

feed1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')

pprint.pprint(feed1)

print('Done with week 1')