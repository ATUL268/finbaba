import pyotp
from kite_trade import *
import pdb


def login_DA3168():

	secret_key_DA3168 = "M6T4JEDJ4L53DHTVQRXZPU3OHDZ3MT7Y"
	totp_DA3168 = pyotp.TOTP(secret_key_DA3168).now()
	totp_DA3168 = str(totp_DA3168)
	# print(totp_DA3168) 

	user_id = "DA3168"       # Login Id
	password = "Share@077"      # Login password
	twofa = totp_DA3168        # Login Pin or TOTP

	enctoken = get_enctoken(user_id, password, twofa)
	
	return enctoken

def login_RA6759():

	secret_key_RA6759 = "KJOCEH3HSAKRUNSSJIQLYZBG7YQIN3NC"
	totp_RA6759 = pyotp.TOTP(secret_key_RA6759).now()
	totp_RA6759 = str(totp_RA6759)
	# print(totp_RA6759) 

	user_id = "RA6759"       # Login Id
	password = "Share@077"      # Login password
	twofa = totp_RA6759        # Login Pin or TOTP

	enctoken = get_enctoken(user_id, password, twofa)
	
	return enctoken



def option_name_finder(name,step_value,multiplier,expiry,CE_PE):
		ltp = sf.LTP(watchlist)
		atm_strike = round(ltp/step_value)* step_value + multiplier*step_value
		option_name = watchlist +expiry+str(atm_strike)+'CE'
		return(option_name)