# Функции в SQL запросах

import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# cursor.execute('SELECT COUNT(*) FROM Users')
# cursor.execute('SELECT COUNT(*) FROM Users WHERE age > 28')
# cursor.execute('SELECT SUM(age) FROM Users')
# cursor.execute('SELECT AVG(age) FROM Users')
# cursor.execute('SELECT MIN(age) FROM Users')
cursor.execute('SELECT MAX(age) FROM Users')

# total_1 = cursor.fetchone()
total_1 = cursor.fetchone()[0]

# total_2 = cursor.fetchall() # пустой список

print(total_1)
# print(total_2)

connection.commit()
connection.close()
