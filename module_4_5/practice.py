# Практика. 1.2

from module_func.sortfunc import *

data_1 = list(map(int, input('enter the numbers separated by a space: ').split()))
data_2 = list(map(int, input('enter the numbers separated by a space: ').split()))
# data_3 = list(map(int, input('Enter a number: ').split()))
# print(data_1)

bubble_sort(data_1)
selection_sort(data_2)

print('Bubble Sort', data_1)
print('Selection Sort', data_2)