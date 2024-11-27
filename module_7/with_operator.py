# Оператор "with"

name = 'sample2.txt'

with open(name) as file:
    for line in file:
        print(line, end='')
    print(file.tell())
