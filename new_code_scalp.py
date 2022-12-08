import xlwings as xw
import datetime
import pandas as pd
import pdb
from pprint import pprint
import time
import os

def init():
	global booked_profit,trade_start,max_diff,slippage,list_1,final,trade_no,status_long ,status_short , soda,final_res,result
	booked_profit = []
	trade_start = 10
	max_diff = 100
	slippage = 1  # Nifty Points

	list_1 = []
	final = {}
	final_res = {}
	trade_no = 1
	soda = 0 

	status_long = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}
	status_short = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}

	result = {'Date'  : None , 'Entry_time' : None ,'exit_time' : None ,'Remark' : None , 'Remark_1' : None , 'Long_price' : None ,'short_price' : None ,'pnl'  : None, 'Cumulative' : None ,'Stoploss' : None ,'Target':None}




init()

input_file  = (r"E:\code_aa\intraday strategy nifty\second")
os.chdir(input_file)

files_list  = os.listdir(input_file)


for file in files_list:

	df = pd.read_csv(file)  # original DataFrame 
	print(file)

	dff  = df.iloc[5:10] # Slicing the Data Frame to find the certain rows . Also making a new dataframe with new Date
	dff = dff[['low' , 'high']] # DataFrame selectiong Rows Jo kam ki hai sari rows me se.
	high = dff['high'].max()
	low = dff['low'].min()
	diff = (high -low)
	target = 400
	df_trade = df.iloc[trade_start:]
	df_trade = df_trade.set_index(df_trade['date'])

	status_long['long'] = high
	status_long['short'] = low
	status_short['long'] = high
	status_short['short'] = low

	

	if diff < max_diff:

		

		for index, ohlc in df_trade.iterrows():
			ltp = df_trade.loc[index]['close']
			# print(f' Candle Time  = {index[11:16]}')
			# print(f' Trade_Number  =  {trade_no}')



			if (ltp > status_long['long']) and (status_long['Traded_long'] == None) and (status_long['done_p'] == None):
				# 
				status_long['Date'] = index[0:10]
				status_long['Long_price'] = ltp
				status_long['Entry_time'] = index[11:16]
				status_long['Target'] = status_long['long'] + target
				status_long['Stoploss'] = status_long['short']
				status_long['LTP'] = ltp
				status_long['Remark'] = 'Long_trade_1'
				status_long['Traded_long'] = 'Yes'
				status_long['Qty'] = 100
				# pdb.set_trace()
				# 

			if (ltp < status_short['short']) and (status_short['Traded_short']) == None and (status_short['done_sl'] == None):
				status_short['Date'] = index[0:10]
				status_short['short_price'] = ltp
				status_short['Entry_time'] = index[11:16]
				status_short['Target'] = status_short['short'] - target
				status_short['Stoploss'] = status_short['long']
				status_short['LTP'] = ltp
				status_short['Remark'] = 'Short_trade_1'
				status_short['Traded_short'] = 'Yes'
				status_short['Qty'] = 100
				# 


			if (status_long['Traded_long'] == 'Yes') and (status_long['Remark'] == 'Long_trade_1') and (status_long['done_p'] == None):
				

				if (ltp < status_long['Stoploss']) :
					status_long['pnl'] = round((ltp - status_long['Long_price']) *status_long['Qty'],2)
					status_long['exit_time'] = index[11:16]
					status_long['Remark_1'] = 'loss_booked'
					
				
				if ltp > status_long['Target'] :
					status_long['pnl'] = round((ltp - status_long['Long_price']) *status_long['Qty'],2)
					status_long['exit_time'] = index[11:16]
					status_long['Remark_1'] = 'Profit_booked'
					

				if index[11:16] == '15:15':
					status_long['pnl'] = round((ltp - status_long['Long_price']) *status_long['Qty'],2)
					status_long['exit_time'] = index[11:16]
					status_long['Remark_1'] = 'Market_over'


			if (status_long['pnl'] != None)  and (status_long['done_sl'] == None) and (status_long['Remark_1'] == 'loss_booked'):
				status_long['completed'] = 'Yes'
				final[trade_no] = status_long
				trade_no = trade_no+1
				result = pd.DataFrame(final).T
				result['Cumulative'] = result.pnl.cumsum()
				result = result[['Date' , 'Entry_time','exit_time','Remark', 'Remark_1', 'Long_price','short_price','pnl' , 'Cumulative','Stoploss','Target']]
				status_long = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}
				status_long['long'] = high
				status_long['short'] = low
				# 

			if (status_long['pnl'] != None)  and (status_long['done_p'] == None) and (status_long['Remark_1'] == 'Profit_booked') :
				status_long['completed'] = 'Yes'
				final[trade_no] = status_long
				trade_no = trade_no+1
				result = pd.DataFrame(final).T
				result['Cumulative'] = result.pnl.cumsum()
				result = result[['Date' , 'Entry_time','exit_time','Remark', 'Remark_1', 'Long_price','short_price','pnl' , 'Cumulative','Stoploss','Target']]
				status_long = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}
				status_long['long'] = high
				status_long['short'] = low
				status_long['Traded_long'] = 'Already_short_booked_Profit'
				status_short['Traded_short'] = 'Already_short_booked_Profit'
				# pdb.set_trace()

			if (status_long['pnl'] != None)  and (status_long['done_MO'] == None) and (status_long['Remark_1'] == 'Market_over') :
				status_long['completed'] = 'Yes'
				final[trade_no] = status_long
				trade_no = trade_no+1
				result = pd.DataFrame(final).T
				result['Cumulative'] = result.pnl.cumsum()
				result = result[['Date' , 'Entry_time','exit_time','Remark', 'Remark_1', 'Long_price','short_price','pnl' , 'Cumulative','Stoploss','Target']]
				status_long = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}
				status_long['long'] = high
				status_long['short'] = low
					
					
			if (status_short['Traded_short'] == 'Yes') and (status_short['Remark'] == 'Short_trade_1') and (status_short['done_sl'] == None):

				if ltp < status_short['Target'] :
					status_short['pnl'] = round((status_short['short_price'] - ltp) *status_short['Qty'],2)
					status_short['exit_time'] = index[11:16]
					status_short['Remark_1'] = 'Profit_booked'
					# 
					
					

				if ltp > status_short['Stoploss'] :
					status_short['pnl'] = round((status_short['short_price'] - ltp) *status_short['Qty'],2)
					status_short['exit_time'] = index[11:16]
					status_short['Remark_1'] = 'loss_booked'
					# 
					
				if index[11:16] == '15:15':
					status_short['pnl'] = round((status_short['short_price'] - ltp) *status_short['Qty'],2)
					status_short['exit_time'] = index[11:16]
					status_short['Remark_1'] = 'Market_over'
					# 
			
			if (status_short['pnl'] != None)  and (status_short['done_sl'] == None) and (status_short['Remark_1'] == 'loss_booked'):
				status_short['completed'] = 'Yes'
				final[trade_no] = status_short
				trade_no = trade_no+1
				result = pd.DataFrame(final).T
				result['Cumulative'] = result.pnl.cumsum()
				result = result[['Date' , 'Entry_time','exit_time','Remark', 'Remark_1', 'Long_price','short_price','pnl' , 'Cumulative','Stoploss','Target']]
				status_short = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}
				status_short['long'] = high
				status_short['short'] = low
				# 

			if (status_short['pnl'] != None)  and (status_short['done_p'] == None) and (status_short['Remark_1'] == 'Profit_booked') :
				status_short['completed'] = 'Yes'
				final[trade_no] = status_short
				trade_no = trade_no+1
				result = pd.DataFrame(final).T
				result['Cumulative'] = result.pnl.cumsum()
				result = result[['Date' , 'Entry_time','exit_time','Remark', 'Remark_1', 'Long_price','short_price','pnl' , 'Cumulative','Stoploss','Target']]
				status_short = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}
				status_short['long'] = high
				status_short['short'] = low
				status_short['Traded_short'] = 'Already_short_booked_Profit'
				status_long['Traded_long'] = 'Already_short_booked_Profit'
				# print(index)
				# 

			if (status_short['pnl'] != None)  and (status_short['done_MO'] == None) and (status_short['Remark_1'] == 'Market_over') :
				status_short['completed'] = 'Yes'
				final[trade_no] = status_short
				trade_no = trade_no+1
				result = pd.DataFrame(final).T
				result['Cumulative'] = result.pnl.cumsum()
				result = result[['Date' , 'Entry_time','exit_time','Remark', 'Remark_1', 'Long_price','short_price','pnl' , 'Cumulative','Stoploss','Target']]
				status_short = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}
				status_short['long'] = high
				status_short['short'] = low
				# print('oooooooooooooooooooooooooo')
				# 


			# if result['pnl'] != None :
			# 	pdb.set_trace()

			# 	if result['pnl'].sum() > 0:
			# 		status_long['done_p'] = 'Done_for_the_day'
			# 		status_short['done_sl'] = 'Done_for_the_day'

		
		status_short = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}
		status_long = {'done_MO' : None ,'done_p' :None ,'done_sl': None, 'completed':None,'Remark_1': None,'long' : None , 'short' : None , 'Date': None , 'short_price': None ,'Entry_time': None , 'Target': None , 'Stoploss': None ,'LTP': None ,'Remark': None ,'Traded_short' : None, 'Traded_long': None , 'Qty': None , 'pnl' :None, 'exit_time' : None , 'Long_price':None}
result = result[['Date' , 'Entry_time','exit_time','Remark', 'Remark_1', 'Long_price','short_price','pnl' , 'Cumulative','Stoploss','Target']]
print(result)			
# pdb.set_trace()