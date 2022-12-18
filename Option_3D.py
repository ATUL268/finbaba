import zrd_login
from pprint import pprint
import pdb
import datetime
import support_file as get
import datetime
import time
import xlwings as xw
import pandas as pd


kite = zrd_login.kite


wb = xw.Book('atul.xlsx')

sht = wb.sheets['Sheet1']

step_value = 100
expiry = '22623'
option_list_CE = []
option_list_PE = []
main_list = []

zrd_watchlist = []

status = {}



ltp = get.LTP('NIFTY BANK')
print(ltp)
atm_strike = round(ltp/step_value)*step_value
# data = 'BANKNIFTY'+expiry+str(atm_strike)+'CE'
for x in range(-13,13):
	strike = atm_strike + (step_value*x)
	data = 'NFO:BANKNIFTY'+ expiry+str(strike)+'CE'
	option_list_CE.append(data)
	strike = atm_strike + (step_value*x)
	data_2 = 'NFO:BANKNIFTY'+expiry+str(strike)+'PE'
	option_list_PE.append(data_2)

zrd_watchlist = (option_list_CE + option_list_PE)
# pdb.set_trace()	


while True:
	try:
			
		val   =  kite.ltp(zrd_watchlist)
		df = pd.DataFrame(val).T
		# pdb.set_trace()
		sht.range('B5').value = df

		ltp = get.LTP('NIFTY BANK')
		atm_strike_main = round(ltp/step_value)*step_value
		
		sht.range('B1').value = ltp
		sht.range('A1').value = 'NIFTY BANK'
		sht.range('D1').value = atm_strike_main
		sht.range('C1').value = 'atm'

		option_list_CE.clear()
		option_list_PE.clear()

		for x in range(-13,13):
			strike = atm_strike_main + (step_value*x)
			data = 'NFO:BANKNIFTY'+expiry+str(strike)+'CE'
			option_list_CE.append(data)

			strike = atm_strike_main + (step_value*x)
			data_2 = 'NFO:BANKNIFTY'+expiry+str(strike)+'PE'
			option_list_PE.append(data_2)
		zrd_watchlist = (option_list_CE + option_list_PE)
	except Exception as e:
		raise e
# pdb.set_trace()
		
	# pprint(option_list_CE)
	# pprint(option_list_PE)
	
# BANKNIFTY 2262 32900 CE
# BANKNIFTY 2262 333000 CE	
# BANKNIFTY 2262 33000 CE



# BANKNIFTY2262332900CE
# BANKNIFTY226232900CE
# # BANKNIFTY2262332000CE

	# print(atm_strike_main)


	# pprint(zrd_watchlist)
# pdb.set_trace()




		# pdb.set_trace()



		# pdb.set_trace()



		


	
	# time.sleep(.5)



