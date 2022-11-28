import zrd_login
from pprint import pprint
from pprint import pprint
import datetime 
kite = zrd_login.kite
import pandas as pd
# import talib as tb
from glob import glob

# margins = kite.margins()





def supdir():
	dirt = dir(support_file01)
	return dirt

# OPENING_BALANCE
def ob():
	open_bal = (margins)['equity']['available']['opening_balance']
	return open_bal

# LIVE_BALANCE
def lb():
	live_bal = (margins)['equity']['available']['live_balance']
	return live_bal

def LTP(name):
	last_price = kite.ltp(['NSE:'+ name])['NSE:'+ name]['last_price']
	return last_price

def LTP_NFO(name):
	last_price = kite.ltp(['NFO:'+name])['NFO:'+name]['last_price']
	return last_price

def ASK(name):
	ask_price = kite.quote(['NSE:'+name])['NSE:'+name]['depth']['sell'][0]['price']
	return ask_price

def ASK_NFO(name):
	ask_price = kite.quote(['NFO:'+name])['NFO:'+name]['depth']['sell'][0]['price']
	return ask_price

def BID(name):
	bid_price = kite.quote(['NSE:'+name])['NSE:'+name]['depth']['buy'][0]['price']
	return bid_price

def BID_NFO(name):
	bid_price = kite.quote(['NFO:'+name])['NFO:'+name]['depth']['buy'][0]['price']
	return bid_price

def OPEN(name):
	opens = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['open']
	return opens

def HIGH(name):
	high = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['high']
	return high

def LOW(name):
	low = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['low']
	return low

def CLOSE(name):
	close = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['close']
	return close

def CLOSE_NFO(name):
	close = kite.quote(['NFO:'+name])['NFO:'+name]['ohlc']['close']
	return close

def VOLUME(name):
	volume = kite.quote(['NSE:'+name])['NSE:'+name]['volume']
	return volume

def OHLC(name):
	opens = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['open']
	high = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['high']
	low = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['low']
	close = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['close']
	return(opens,high,low,close)

def OHLCV(name):
	opens = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['open']
	high = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['high']
	low = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['low']
	close = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['close']
	volume = kite.quote(['NSE:'+name])['NSE:'+name]['volume']
	return(opens,high,low,close,volume)

def OHLCVLTP(name):
	opens = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['open']
	high = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['high']
	low = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['low']
	close = kite.quote(['NSE:'+name])['NSE:'+name]['ohlc']['close']
	volume = kite.quote(['NSE:'+name])['NSE:'+name]['volume']
	last_price = kite.ltp(['NSE:'+name])['NSE:'+name]['last_price']
	return(opens,high,low,close,volume,last_price)


def OI(name):
	oi = kite.quote(['NFO:'+name])['NFO:'+name]['oi']
	return oi

def VNFO(name):
	vnfo = kite.quote(['NFO:'+name])['NFO:'+name]['volume']
	return vnfo

def option_name_finder(name,step_value,multiplier,expiry,CE_PE):
		ltp = sf.LTP(watchlist)
		atm_strike = round(ltp/step_value)* step_value + multiplier*step_value
		option_name = watchlist +expiry+str(atm_strike)+'CE'
		return(option_name)

def histo_data(name,segment,delta,interval,continuous,oi):
	token = kite.ltp([segment + name])[segment + name]['instrument_token']
	to_date = datetime.datetime.now().date()
	from_date = to_date - datetime.timedelta(days = delta)
	hd = kite.historical_data(instrument_token = token, from_date = from_date, to_date = to_date, interval = interval, continuous = False, oi = False)
	hd = pd.DataFrame(hd)
	return hd

def histo_data1(name,segment,delta,delta1,interval,continuous,oi):
	token = kite.ltp([segment + name])[segment + name]['instrument_token']
	to_date = datetime.datetime.now().date()
	to_date1 = to_date - datetime.timedelta(days = delta1)
	from_date = to_date - datetime.timedelta(days = delta)
	hd = kite.historical_data(instrument_token = token, from_date = from_date, to_date = to_date1, interval = interval, continuous = False, oi = False)
	hd = pd.DataFrame(hd)
	return hd

def read_data(name):
	near_ext = '21AUGFUT'
	far_ext = '21SEPFUT'

	near_name = name + near_ext + '.csv'
	far_name = name + far_ext + '.csv'

	near = pd.read_csv("near" + "\\" + near_name)
	far = pd.read_csv("far" + "\\" + far_name)

	near = near.set_index(near['date'])
	far = far.set_index(far['date'])

	return near, far
	

def read_data01(name):
	name1 = name + '.csv'
	namersi = pd.read_csv("RSI(DAY)" + "\\" + name1)
	# namersi = namersi.set_index(namersi['date'])
	return namersi

def hist_download_merge(i,too,fro,name,names,rsi,stok_file,mergedatas,intervl,segment):
	for i in range (7):
		token = kite.ltp([segment + name])[segment + name]['instrument_token']
		to_date = datetime.datetime.now().date()
		to_date1 = to_date - datetime.timedelta(days = fro[i])
		from_date = to_date - datetime.timedelta(days = too[i])
		df = kite.historical_data(instrument_token = token, from_date = from_date, to_date = to_date1, interval = intervl, continuous = False, oi = False)
		df = pd.DataFrame(df)
		df['rsi'] = tb.RSI(df['close'], timeperiod = rsi)
		df['rsi_pre'] = df['rsi'].shift(1)
		name1 = names + str(7-i)
		df.to_csv('RSI(min)' + '\\' + name1 + '.csv')
	stock_files = sorted(glob(stok_file))
	mergedata = pd.concat(pd.read_csv(stock_file) for stock_file in stock_files)
	mergedata.to_csv(mergedatas)
	return df,mergedata

def read_data02(name):
	name1 = name + '.csv'
	namersi = pd.read_csv("Result_Storage" + "\\" + name1)
	namersi = namersi.set_index(namersi['date'])
	return namersi
def read_data03(name):
	name1 = name + '.csv'
	namersi = pd.read_csv("Result_Storage1" + "\\" + name1)
	namersi = namersi.set_index(namersi['date'])
	return namersi

 # def add_days_from_index(date, days):
        #         add_date = pd.to_datetime(date) + timedelta(days=days)
        #         add_date = add_date.strftime("%Y-%m-%d")
        #         return add_date
        #     # print(index[:10])
        #     # x = 0
        #     index_add = add_days_from_index(index[:10], 1)               
        #     # if index[:10] == index_add:
        #     print(index[:10],index_add)
            # x = x + 1



