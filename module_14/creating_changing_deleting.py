# Создание, Изменение и Удаление элементов

import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# cursor.execute('INSERT INTO Users(username, email, age) VALUES(?, ?, ?)', ('new_user', 'test@mail.com', '23'))

# for i in range(30, 40):
#     cursor.execute('INSERT INTO Users(username, email, age) VALUES(?, ?, ?)', (f'new_user_{i}', f'test_{i}@mail.com', f'{10 + i}'))

# cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (40, 'new_user'))

cursor.execute('DELETE FROM Users WHERE username = ?', ('new_user', ))

connection.commit()
connection.close()