import sqlite3

connection = sqlite3.connect('SVPCC.db')
cursor = connection.cursor()
result = cursor.execute('''SELECT * FROM SpringCrops''')
fetchAll = result.fetchall()
springCrops = {}
for item in fetchAll:
    springCrops[item[1]] = item

springCrops.pop(None)
print (springCrops)