from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pdb
import pandas as pd
import datetime
import os


api_k = "6dwrrcjeowxqco0b"  # api_key
api_s = "bgectyh4xfl0sa79hr55n983k6wzkk2u"  # api_secret
filename = str(datetime.datetime.now().date()) + ' token' + '.txt'


def read_access_token_from_file():
	file = open(filename, 'r+')
	access_token = file.read()
	file.close()
	return access_token


def send_access_token_to_file(access_token):	
	file = open(filename, 'w')
	file.write(access_token)
	file.close()


def get_login(api_k, api_s):
	global kws, kite
	kite = KiteConnect(api_key=api_k)
	print("Logging into zerodha")


	if filename not in os.listdir():

		print("[*] Generate Request Token : ", kite.login_url())
		request_tkn = input("[*] Enter Your Request Token Here : ")
		data = kite.generate_session(request_tkn, api_secret=api_s)
		access_token = data["access_token"]
		kite.set_access_token(access_token)
		kws = KiteTicker(api_k, access_token)
		send_access_token_to_file(access_token)

	elif filename in os.listdir():
		print("You have already loggged in for today")
		access_token = read_access_token_from_file()
		kite.set_access_token(access_token)
		kws = KiteTicker(api_k, access_token)

	return kite

kite = get_login(api_k, api_s)
