#!/home/nextgen/venv/bin/python3

import sqlite3
import datetime
from functions import getround
from functions import nextround
from functions import inisell

#set constants
gap = 0.005
#end set constants


R = getround()
t = R[0]
roundbegin = R[1]

roundbegin = datetime.datetime.strptime(roundbegin, '%Y-%m-%d %H:%M:%S')

now = datetime.datetime.utcnow()

print(t)

print("roundbegin:",roundbegin)
print("now:",now)
print(now -roundbegin)

stale = now - roundbegin >= datetime.timedelta(hours=48)

print(stale)

conn = sqlite3.connect('Data.db')
c = conn.cursor()

temp_table = c.execute('''SELECT * FROM BUYORDERS WHERE round = ?''',(t,))

buys = []
for row in temp_table:
	buys.append(row)

print(buys)

temp_table = c.execute('''SELECT * FROM Selllevels WHERE round = ?''',(t,))

sells = []
for row in temp_table:
	sells.append(row)

print(sells)

conn.commit()
conn.close()

if len(buys)!=0:
	print("Check if stuff changed")
elif len(sells)!=0:
	print("Check if sells changed")
	#If stuff did not change and `stale` then `nextround()`
else:
	print("Place sell orders")
	inisell(gap)
