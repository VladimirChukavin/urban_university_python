# Модули и пакеты
# Модули. Способы импортирования кода
# Создание пакетов и компилированные файлы

# import module_two as m2
# from module_two import a, b, say_hi
# from module_two import say_hi as sh
# import sys
from .module_two import say_hi

print("Hi from module_one")
# print(dir(module_two))

# print(module_two.a)

# print(m2.a, m2.b)

# module_two.say_hi()

# m2.say_hi()

# print(a, b)

# say_hi()

# print(m2.__name__)

# sh()

# for path in sys.path:
# print(path)

say_hi()
