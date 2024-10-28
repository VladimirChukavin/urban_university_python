# Модули и пакеты
# Модули. Способы импортирования кода
# Создание пакетов и компилированные файлы


def say_hi():
    a = 5
    b = 11
    print("Hi from function module_two")
    return a, b


print(__name__)
if __name__ == "__main__":
    say_hi()
