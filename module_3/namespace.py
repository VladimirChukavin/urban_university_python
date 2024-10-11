# Пространство имен

# Встроенное, локальное, глобальное

a = 4
b = 2

print(a, b)

def printer():
    # local namespace
    global a, b
    a = 'one'
    b = 'two'
    c = 3
    d = 1
    print(c, d, 'local')
    print(a, b, 'global')

printer()
# print(c, d) # error
print(a, b)
