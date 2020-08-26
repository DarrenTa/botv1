#!/home/nextgen/venv/bin/python3

import sqlite3

conn = sqlite3.connect('Data.db')
c = conn.cursor()

round_table = c.execute('''SELECT * FROM Round''')

table = []

for row in round_table:
	table.append(row)

for row in table:
	print(row)

conn.commit()
conn.close()
