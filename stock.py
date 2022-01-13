# import requests
# from bs4 import BeautifulSoup
import pandas as pd
import lxml
import json
from py5paisa import FivePaisaClient
import time
import datetime as dt
# local imports
import symbolOf
from nifty import Stock


stock = Stock('RELIANCE')
indexSymbol = symbolOf.niftyIndex(200)
# print(indexSymbol)
print(len(indexSymbol))
print(stock.scripCode())
print(stock.get_scripName(2885))