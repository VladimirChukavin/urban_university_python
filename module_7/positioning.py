# Позиционирование в файле

from pprint import pprint

name2 = "sample3.txt"
file = open(name2, "r")
print(file.writable())
print(file.readable())
print(file.seekable())
print(file.name)
print(file.buffer)
print(file.closed)
print(file.tell())
pprint(file.read())
# file.seek(45)
# file.write("New text line.")
print(file.tell())
file.close()
