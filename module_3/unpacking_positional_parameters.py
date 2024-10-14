# Распаковка позиционных параметров

def print_params(*args):
    print(args, *args)


print_params(1, 2, 3, 4, 5)
print_params()


def print_list(a, b, c):
    print(a, b, c)


list_ = [1, 2, 3]
print_list(list_, 5, 6)
print_list(0, 0, list_)
print_list(*list_)

dict_ = {'a': 7, 'b': 8, 'c': 9}
print_list(**dict_)


def print_dict(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


print_dict(**dict_)


def print_all(*args, **kwargs):
    print(*args, kwargs)


print_all(*list_, **dict_)
