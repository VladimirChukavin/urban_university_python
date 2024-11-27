# Режимы открытия файлов

from pprint import pprint

name = "sample.txt"

file = open(name, "r")
# print(file)

pprint(file.read())
file.close()

name2 = "sample3.txt"
file = open(name2, "w")
file.write("This is sixth line.")
file.close()

file = open(name2, "a")
file.write("\nThis is seventh line.")
file.close()
