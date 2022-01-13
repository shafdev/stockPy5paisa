import datetime as dt
import pandas as pd
import loginTo5paisa
from py5paisa import FivePaisaClient
client = loginTo5paisa.client


class Stock:
    def __init__(self,tickerName):
        self.tickerName = tickerName
        self.end = dt.date.today()
        self.date_range = pd.date_range(end=self.end,periods=32,freq='B')
        self.start = self.date_range[0]
        #to change the avg volume change the periods
        
    def scripmaster(self):
        #"https://images.5paisa.com/website/scripmaster-csv-format.csv"
        scrip_codes = pd.read_csv("./csv/scripmaster-csv-format.csv")
        mask1 = scrip_codes['Series']=='EQ'
        mask2 = scrip_codes['Exch']=='N'
        mask3 = scrip_codes['Series']=='BE'
        eq_scrip = scrip_codes[(mask1 & mask2) | mask3]
        scrip_code_list = eq_scrip[["Name","Scripcode","Exch","ExchType"]]
        return scrip_code_list
    
    def scripCode(self):
        #maskNSE = scrip_code_list['Name'] == self.tickerName
        maskNSE = self.scripmaster()['Name'] == self.tickerName
        nse = self.scripmaster()[maskNSE]
        indexNum = self.scripmaster()[maskNSE].index[0]
        code = nse["Scripcode"][indexNum]
        return code
    
    #gets 30 DAYS AVG VOLUME
    def get_avgVolume(self):
        try:
            code = self.scripCode()
            strCode = str(code)
            df=client.historical_data('N','C',strCode,'1d',self.start,self.end)
            vol_r = df['Volume'].mean()/100000
            volume = round(vol_r,5)
        except:
            pass
        return volume
    
    #gets Live VOLUME
    def get_liveVolume(self):
        z=str(self.scripCode())
        a=[{"Exchange":"N","ExchangeType":"C","ScripCode":z}]
        df1 = client.fetch_market_depth(a)
        volume = df1['Data'][0]['Volume']
        volume = int(volume)/100000
        return volume
    
    def get_scripName(self,tickerCode):
        #mask = scrip_code_list['Scripcode'] == tickerCode
        mask = self.scripmaster()['Scripcode'] == tickerCode
        indexNum = self.scripmaster()[mask].index[0]
        scripName = self.scripmaster()['Name'][indexNum]
        return scripName
    
    #gets live percent change
    def get_pChange(self):
        code = self.scripCode()
        codestr = str(code)
        a=[{"Exchange":"N","ExchangeType":"C","ScripCode":codestr}]
        listData = client.fetch_market_depth(a)['Data'][0]
        calcPercent = float(listData['NetChange'])/float(listData['Close'])*100
        percentChange = round(calcPercent,2)
        return percentChange


# stock = Stock('ONGC')
# print(stock.get_pChange())
# print(stock.get_avgVolume())
# print(stock.get_liveVolume())