# Домашняя работа по уроку "Распаковка позиционных параметров"

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=8, c=False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['test', 465.846, False]
values_dict = {'a': 'one', 'b': True, 'c': 416}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
