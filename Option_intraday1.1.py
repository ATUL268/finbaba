# import zrd_login
# kite = zrd_login.kite
from pprint import pprint
import pdb
import pandas as pd
import support_file as get
import datetime
import time
from datetime import datetime
import os ,time
from dateutil.parser import parse


def init():
	global sl,final_result, target,status,entry_time,step_value,input_file,output_file,atm_list,atm_strike,cumulative ,CE_ltp,PE_ltp,exit_time,qty,trade_no,index_pe
	final_result = {}
	step_value = 100
	input_file = (r'F:\code_atul\Back_Test_data')
	output_file = "F:/code_atul/database/Final"
	atm_strike = None
	trade_no = 1
	atm_list = []
	cumulative = []
	status = {'sell_CE' : None,'sell_PE' : None , 'stoploss_CE' : None,'targett_CE' :None,  'traded_CE' : None , 'stoploss_PE' : None, 'targett_PE' : None,'traded_PE' : None,'remark_CE' : None,'Buy_CE' : None, 'remark_PE' : None, 'Buy_PE' : None, 'pnl_CE' : None , 'pnl_PE' : None,'ATM' : None,'Date' : None, 'Index_LTP' : None,'Day': None, 'PNL_Strategy': None,'Drawdown' :None}

	sl = 0.06
	target = 0.84
	qty = 50
	entry_time  = '09:16'
	exit_time = '14:55'
	

	







init()


os.chdir('F:/code_atul/Back_Test_data/')

files_list  = os.listdir('F:/code_atul/Back_Test_data/')
for file in files_list:
	print(file)
	df = pd.read_csv('F:/code_atul/Back_Test_data/' + 'Banknifty.csv' )
	df = df.set_index(df['date'])

	for index, ohlc in df.iterrows():
		date_name  = index[0:10]  
		date_time  = index[11:16]# print output = '2022-05-31'
		
		if (file  == date_name) and (date_time == entry_time) :
			os.chdir('F:/code_atul/Back_Test_data/' + '/' + file)
			list_2 = os.listdir('F:/code_atul/Back_Test_data/' + '/' + file)
			list_2 = list_2[0]
			print(list_2)
			os.chdir('F:/code_atul/Back_Test_data/' + '/' + file + '/' + list_2)
			final_list = os.listdir('F:/code_atul/Back_Test_data/' + '/' + file + '/' + list_2)
			ltp  = df.loc[index]['open']
			atm_strike = str(round(ltp/step_value)*step_value)

			for strike in final_list:

				if strike[14:19] == atm_strike and strike[19:21] == 'CE':
					df_2  = pd.read_csv(strike)
					df_2 = df_2.set_index(df_2['date'])

					CE_ltp = df_2.loc[index]['open']

					status["sell_CE"] = CE_ltp
					status['stoploss_CE'] = round((sl*CE_ltp) + (CE_ltp),2)
					status['targett_CE'] = round((CE_ltp) - (target*CE_ltp),2)
					status['traded_CE'] = 'YES'

				
				if strike[14:19] == atm_strike and strike[19:21] == 'PE':
					df_3  = pd.read_csv(strike)
					df_3 = df_3.set_index(df_3['date'])
					PE_ltp = df_3.loc[index]['open']

					status["sell_PE"] = PE_ltp
					status['stoploss_PE'] = round((sl*PE_ltp) + (PE_ltp),2)
					status['targett_PE'] = round((PE_ltp) - (target*PE_ltp),2)
					status['traded_PE'] = 'YES'


				if status['traded_CE'] == 'YES'  and status['traded_PE'] == 'YES':
					# pdb.set_trace()
					ce = strike[0:19] + 'CE' + '.csv'
					pe = strike[0:19] + 'PE' + '.csv'

					df_20  = pd.read_csv(ce)
					df_20 = df_20.set_index(df_20['date'])
					df_3  = pd.read_csv(pe)
					df_3 = df_3.set_index(df_3['date'])

	

					for indexx, ohlc_ce in df_20.iterrows():

						ltp_ce = df_20.loc[indexx]['open']

						indexx_c = parse(indexx)
						entry_time_c = indexx[0:10] + ' ' +entry_time + ':' + '00+05:30'
						entry_time_c = parse(entry_time_c)
						# print(ltp_ce,indexx,strike)

						if (indexx_c > entry_time_c and status['traded_CE'] == 'YES') and (indexx[11:16] == exit_time) or (ltp_ce > status['stoploss_CE']) or (ltp_ce < status['targett_CE']) :

							# pdb.set_trace()
							if (indexx[11:16] == exit_time):
								status['remark_CE'] = 'Market_over'
								status['pnl_CE'] = round((status['sell_CE']-ltp_ce)*qty,2)
								status['Buy_CE'] = ltp_ce


							if (ltp_ce > status['stoploss_CE']):
								status['remark_CE'] = 'Stoploss_Hit'
								status['pnl_CE'] = round((status['sell_CE']-status['stoploss_CE'])*qty,2)
								status['Buy_CE'] = status['stoploss_CE']


							if (ltp_ce < status['targett_CE']):
								status['remark_CE'] = 'Target_Hit'
								status['pnl_CE'] = round((status['sell_CE']-status['targett_CE'])*qty,2)
								status['Buy_CE'] = status['targett_CE']

							
					for index_pe, ohlc_pe in df_3.iterrows():
						# print('df_3')

						ltp_pe = df_3.loc[index_pe]['open']
						index_pe_c = parse(index_pe)
						entry_time_c = index_pe[0:10] + ' ' + entry_time + ':' + '00+05:30'
						entry_time_c = parse(entry_time_c)
						# print(ltp_ce,index_pe,strike)

						if ((index_pe_c > entry_time_c) and status['traded_PE'] == 'YES') and ((index_pe[11:16] == exit_time) or (ltp_pe > status['stoploss_PE']) or (ltp_pe < status['targett_PE'])) :
							# pdb.set_trace()

							if (index_pe[11:16] == exit_time):
								status['remark_PE'] = 'Market_over'
								status['pnl_PE'] = round((status['sell_PE']-ltp_pe)*qty,2)
								status['Buy_PE'] = ltp_pe


							if (ltp_pe > status['stoploss_PE']):
								status['remark_PE'] = 'Stoploss_Hit'
								status['pnl_PE'] = round((status['sell_PE']-status['stoploss_PE'])*qty,2)
								status['Buy_PE'] = status['stoploss_PE']


							if (ltp_pe < status['targett_PE']):
								status['remark_PE'] = 'Target_Hit'
								status['pnl_PE'] = round((status['sell_PE']-status['targett_PE'])*qty,2)
								status['Buy_PE'] = status['targett_PE']

							# pdb.set_trace()
							trade_date = parse(file)
							trade_day = trade_date.strftime("%A")
							status['ATM'] = atm_strike
							status['Date'] = file
							status['Day'] = trade_day
							status['Index_LTP'] = df.loc[index]['open']
							status['PNL_Strategy'] = status['pnl_PE'] + status['pnl_CE']
							cumulative.append(status['PNL_Strategy'])

							status['Drawdown'] = sum(cumulative)
							final_result[trade_no] = status
							status = {'sell_CE' : None,'sell_PE' : None , 'stoploss_CE' : None,'targett_CE' :None,  'traded_CE' : None , 'stoploss_PE' : None, 'targett_PE' : None,'traded_PE' : None,'remark_CE' : None,'Buy_CE' : None, 'remark_PE' : None, 'Buy_PE' : None, 'pnl_CE' : None , 'pnl_PE' : None,'ATM' : None,'Date' : None,'Index_LTP' : None,'Day': None , 'PNL_Strategy' :None,'Drawdown' :None}
							trade_no = trade_no + 1
							print(trade_no)



last = pd.DataFrame(final_result).T
print(last)


last.to_excel('result501.xlsx')







