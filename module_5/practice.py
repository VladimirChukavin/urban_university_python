# Практика (Система регистрации на классах). 1.1
# Практика. 1.2
# Практика. 1.3

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержит логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password_in = input('Введите пароль: ')
            if login in database.data:
                if password_in == database.data[login]:
                    print(f'Успешный вход для пользователя {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден')
        if choice == 2:
            user = User(input('Логин: '), password1 := input('Пароль: '),
                        password2 := input('Повторите пароль: '))
            if password1 != password2:
                print('Пароли не совпадают, попробуйте еще раз!')
                # exit()
                continue
            database.add_user(user.username, user.password)
        # print(database.data)
