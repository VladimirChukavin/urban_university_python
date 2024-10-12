# Способы вызова функции по умолчанию

def print_params(a, b, c):
    print(a, b, c)


# print_params() # error
print_params(1, 2, 3)


def default_params(a=1, b=2, c=3):
    print(a, b, c)


default_params()
default_params(4, 5, 6)
