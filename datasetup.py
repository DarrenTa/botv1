#!/home/nextgen/venv/bin/python3

import sqlite3
import json
from functions import nextround


conn = sqlite3.connect('Data.db')
c = conn.cursor()

c.execute('''CREATE TABLE Round ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [start_time] TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

c.execute('''CREATE TABLE Activesells ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [round] INTEGER, [order_id] INTEGER, [price] REAL, [amount] REAL, [time] TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

c.execute('''CREATE TABLE Selllevels ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [round] INTEGER, [level] INTEGER, [order_id] INTEGER, [price] REAL, [amount] REAL)''')

c.execute('''CREATE TABLE Buyorders ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [round] INTEGER, [time_placed] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, [amount] REAL, [price] REAL)''')

conn.commit()
conn.close()

nextround()
