tuple_1 = 1, 2, 3, 4, 5
print(tuple_1)
print(type(tuple_1))
tuple_2 = (1, 2, 3)
print(tuple_2)
tuple_3 = tuple([1, 2, 3, 4])
print(tuple_3)
print(tuple_3[1])
tuple_4 = (1, 2, 3, 4)
list_4 = [1, 2, 3, 4]
print(tuple_4.__sizeof__())
print(list_4.__sizeof__())
tuple_5 = ([10, 20], 0)
print(tuple_5)
tuple_5[0].append(30)
print(tuple_5)
tuple_6 = tuple_2 + tuple_5
print(tuple_6)
tuple_7 = tuple_4 * 3
print(tuple_7)
tuple_8 = 8,
print(tuple_8)

# homework module_1_5.py
immutable_var = ('test', 1, True)
print('Immutable tuple:', immutable_var)
# immutable_var[0] = 'modified' # TypeError: 'tuple' object does not support item assignment.
# Кортежи нельзя изменять, потому что они были разработаны таким образом.
# Это сводится к эффективности. Когда вы знаете, что последовательность не может измениться,
# вы можете выделить для нее точно нужный объем памяти и вы можете хранить только одну
# копию данной последовательности независимо от того, сколько раз она использовалась
# в программе.

mutable_list = ['test', 1, True]
mutable_list.append('modified')
print('Mutable list:', mutable_list)