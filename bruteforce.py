import pdb
import pandas as pd


ma_small_values  = [3,4]
ma_big_values  = [ 10 , 12 , 14 , 16 , 18 , 20 , 22 , 24 , 26 ]

all_combs = {}
comb_no = 0


for ma_small_value in ma_small_values:
	for ma_big_value in ma_big_values:
		comb =  {'ma_small_value' : ma_small_value , 'ma_big_value' : ma_big_value }
		comb_no = comb_no + 1
		print(comb_no)
		all_combs[comb_no] = comb

combs = pd.DataFrame(all_combs).T
combs.to_excel('combinations_bacha.xlsx')
