import pandas as pd
import datetime as dt
import time
from py5paisa import FivePaisaClient
import numpy as np
from pygame import mixer
cred={
    "APP_NAME":"5P59739795",
    "APP_SOURCE":"7664",
    "USER_ID":"oBlixXtNQ",
    "PASSWORD":"RHRiDhtxN",
    "USER_KEY":"dhGVcNwjbjM05IAl7U3Ue5UW",
    "ENCRYPTION_KEY":"vJMuM7P1KNiAEOTCJJE5v3D"
    }
client = FivePaisaClient(email="Your_email_here", passwd="Your_password_here", dob="dateOfBirth",cred=cred)
client.login()

# ###############################

def get_futureScrip(month,nif_bn):
    '''nif_bn:0/1 -- 1 is for nifty and 0 is for banknifty'''
    scrip_codes = pd.read_csv("scripmaster-csv-format.csv")
    niftyMask = scrip_codes["ISIN"] == "NIFTY"
    bnMask = scrip_codes["ISIN"] == "BANKNIFTY"
    scrip_codes = scrip_codes[niftyMask | bnMask]
    cpMask = scrip_codes["CpType"] == 'XX'
    maskfilter = scrip_codes[cpMask]["FullName"].str.contains(month)
    indexNum = scrip_codes[cpMask]["FullName"][maskfilter].index[nif_bn]
    scrip_codes.loc[indexNum]
    name = scrip_codes.loc[indexNum]["Name"]
    scripcode = scrip_codes.loc[indexNum]["Scripcode"]
    return scripcode

#gets futures scripcode just by entering month
get_futureScrip("Jan",0)
get_futureScrip("Jan",1)

def load_music(load):
    mixer.init()
    mixer.music.load(r'C:\Users\VIC\Downloads\sounds\{load}.wav'.format(load=load))
    
def play():
    mixer.music.play()

def createDateRange(freq):
    '''Input the frequency of time to create the date range 
    |For market timing only'''
    
    dateRange = pd.date_range(start='9:15' ,end='15:30',freq=f"{freq}min")
    dateRange = dateRange.strftime('%H:%M')
    return dateRange

def now():
    now = dt.datetime.now() 
    now = pd.to_datetime(now).strftime('%H:%M')
    return now

def check_candle(Open,Close):
    if Open<Close:
        print('Green Candle') 
    if Close<Open:
        print('Red Candle')
        
load_music('pop-up')
# play()
dateRange = createDateRange(5)
today = dt.datetime.now().strftime("%Y-%m-%d")

#1 is for nifty future ,and 0 is for banknifty future
futureScripCode = get_futureScrip("Jan",1)



####################################################################

# runs the code when time now is in the dateRange.
# future_alert(5) --> it will alret for 5 minute candle  , 

def future_alert(minute):
    while True:
        for i in range(len(dateRange)):

            if now() == dateRange[i]:
                df=client.historical_data('N','D',futureScripCode,f'{minute}m',today,today)
                volume = df.loc[len(df)-1]['Volume']
                Open = df.loc[len(df)-1]['Open']
                Close = df.loc[len(df)-1]['Close']
                datetime = df.loc[len(df)-1]['Datetime']
                datetime = pd.to_datetime(datetime).strftime("%H:%M")

                #When the 5 min volume is greater than 1l notification will be played
                if volume > 100000:
                    check_candle(Open,Close)
                    play()
                    print(datetime , volume)

                #print(df)
                print('something')
                time.sleep(60*minute)
            else:
                continue

