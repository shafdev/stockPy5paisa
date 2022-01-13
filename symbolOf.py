import pandas as pd

# gets Index symbols
def niftyIndex(getsymbol):
    if getsymbol == 'midcap':
        nifty_list = pd.read_csv('https://archives.nseindia.com/content/indices/ind_niftymidcap100list.csv')
        nifty_symbols = nifty_list['Symbol']
        return nifty_symbols 
    if getsymbol == 'smallcap':
        nifty_list = pd.read_csv('https://archives.nseindia.com/content/indices/ind_niftysmallcap50list.csv')
        nifty_symbols = nifty_list['Symbol']
        return nifty_symbols 
    else:
        nifty_list = pd.read_csv(f'https://archives.nseindia.com/content/indices/ind_nifty{getsymbol}list.csv')
        nifty_symbols = nifty_list['Symbol']
        return nifty_symbols 
        
# nif_100 = niftyIndex(100)