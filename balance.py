#!/home/nextgen/venv/bin/python3

import ccxt
import json

coinex = ccxt.coinex({
        'apiKey': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'secret': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
})

balances = coinex.fetch_balance()

#print(balances)

if 'DASH' in balances:
	print("DASH: ",balances['DASH'])
if 'BTC' in balances:
	print("BTC:  ",balances['BTC'])
