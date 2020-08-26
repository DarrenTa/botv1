#!/home/nextgen/venv/bin/python3

import sqlite3
import ccxt
from math import floor
from time import sleep


coinex = ccxt.coinex({
        'apiKey': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'secret': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
})

def rounddown(x,n):
    #x should be float
    return floor(x*10**n)/10**n

def nextround():
	conn = sqlite3.connect('Data.db')
	c = conn.cursor()
	c.execute('''INSERT INTO Round DEFAULT VALUES''')
	conn.commit()
	conn.close()

def getround():
	conn = sqlite3.connect('Data.db')
	c = conn.cursor()
	round = c.execute('''SELECT id, start_time FROM Round ORDER BY id DESC LIMIT 1''')
	x= []
	for row in round:
		for y in row:
			x.append(y)
	conn.commit()
	conn.close()
	return x

def inisell(gapratio):
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    R= getround()
    t = R[0]
    epsilon = 10**-8
    amtratios = [3.0]
    for k in range(0,19):
        amtratios.append((4.0/3.0)**k + k * epsilon)
    #print(amtratios)
    #print("sum:",sum(amtratios))
    lastmarketprice = coinex.fetchTicker('DASH/BTC')['last']
    baseprice = rounddown(lastmarketprice + 3*epsilon,8)
    gap = rounddown(gapratio*baseprice+epsilon,8)
    print(lastmarketprice)
    balances = coinex.fetch_balance()
    if 'DASH' not in balances:
            print('No Dash to Sell')
            return
    freedash = balances['DASH']['free']
    print("DASH:",freedash)
    baseamount = freedash/sum(amtratios)
    baseamount = rounddown(baseamount,8)
    print("baseamount:",baseamount)
    amts = []
    for k in range(0,20):
        amts.append(rounddown(baseamount*amtratios[k],8))
    print(amts)
    if min(amts)<= .05: return
    #print(len(amts)==len(amtratios))
    prices = [baseprice]
    for k in range(0,19):
        prices.append(rounddown(baseprice + (4+k)*gap,8))
    print(prices)
    #Place API call to place sell orders here.  Make sure to sleep as there are 20 of them.
    zero = 0
    for k in range(0,20):
        c.execute('''INSERT INTO Selllevels (round,level,order_id,price,amount) \
            VALUES (?,?,?,?,?)''',(t,k,zero,prices[k],amts[k]))

    conn.commit()
    conn.close()
