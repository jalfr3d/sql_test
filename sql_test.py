import sqlite3

# Establish a connection and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

# Get all rows and all columns by order
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cur.fetchall())

# Get all rows and all columns by order
cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
print(cur.fetchall())

# Get all rows where asn is less than 300
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(cur.fetchall())

# Get all rows where asn is less than 300
cur.execute("SELECT * FROM 'ips' WHERE asn = 144")
print(cur.fetchall())

# Get all rows where asn is less than 300 and domain contain sa in the end
cur.execute("SELECT * FROM 'ips' WHERE asn < 300 AND domain LIKE '%sa'")
print(cur.fetchall())