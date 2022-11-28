from pprint import pprint
import pdb 
import pandas as pd
import time
import zrd_login
import datetime
import support_file01 as sf
import pyotp
from kite_trade import *
import login as ln

# import talib

def init():
	global name, Status,final_result, kite, breakin_time, breakout_time, wb, sht, Qty, name1, Stoploss,Target,tradeno
	kite = zrd_login.kite
	Status = {'Date': None, 'Entry_time': None, 'Qty': None, 'Target_CE_ATM': None, 'Stoploss_CE_ATM':None, 'Target_PE_ATM': None, 'Stoploss_PE_ATM':None, 'PNL_CE_ATM': None, 'PNL_PE_ATM': None, 'Traded': None, 'Traded_ok':None, 'Traded_CE':None, 'Traded_PE':None,'Remark_CE_ATM': None, 'Remark_PE_ATM': None, 'Exit_time_CE_ATM': None, 'Exit_time_PE_ATM': None, 'Sell_CE_ATM0': None, 'Sell_PE_ATM0': None, 'Buy_CE_ATM1': None, 'Buy_PE_ATM1': None, 'ltp_CE_ATM': None, 'ltp_PE_ATM': None, 'CE_ATM0': None, 'PE_ATM0': None,'sell_orderid_CE': None, 'sell_orderid_PE': None, 'buy_orderid_CE': None, 'buy_orderid_PE': None, 'break_CE':None,'break_PE':None}
	# final_result = {}
	# tradeno = 0
	# breakin_time = datetime.time(12,38)
	# breakout_time = datetime.time(14,55)
	Qty = 2
	name = 'IDEA'
	# Stoploss = 0.14
	# Target = 0.84
	# pdb.set_trace()
 



init()


# print(kite.margins())
sell_orderid_CE = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol= name, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity= 4, product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET, price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
kite = KiteApp(ln.login_DA3168())
sell_orderid_PE = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol= name, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity= Qty, product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET, price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
kite = KiteApp(ln.login_RA6759())
sell_orderid_TE = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol= name, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity= Qty, product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET, price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)

# print(kite.margins())
# pdb.set_trace()

print(sell_orderid_PE,sell_orderid_CE,sell_orderid_TE)