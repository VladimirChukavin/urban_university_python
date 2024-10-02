# Словари и множества

set_ = {1, 2, 3, 4, 5, 6, 1, 2, 3, 0, 'test', True, (34, 42, 998)}
print(set_)
print(type(set_))
list_ = [1, 1, 2, 3, 4, 4, 9]
print(set(list_))
set_.discard(1)
set_.discard(11) # no error
print(set_)
set_.remove(2)
# set_.remove(20) # error
print(set_)
num = set_.pop()
print(set_)
print(num)
num = set_.pop()
print(num)
set_.add(7)
print(set_)

# homework module_1_6.py
my_set = {1, 1, 'test', 'test', 546.458}
print(my_set)
my_set.add(2)
my_set.add((4, 5))
my_set.discard('test')
print(my_set)