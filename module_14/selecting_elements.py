# Выбор элементов

import sqlite3
import random

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# for i in range(50):
#     cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (str(random.randint(20, 50)), f'new_user_{i}'))

# SELECT FROM WHERE GROUP BY HAVING
# cursor.execute('SELECT * FROM Users')
# cursor.execute('SELECT username, age FROM Users WHERE age > ?', (29, ))
cursor.execute('SELECT username, age FROM Users GROUP BY age')

users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()