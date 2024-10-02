# Словари и множества

phone_book = {'Lane': [65484638, 71684688], 'Max': 86857731}
print(phone_book)
print(phone_book['Max'])
phone_book['Lane'] = 18488468
print(phone_book)
phone_book['John'] = 4234168468
print(phone_book)
print(len(phone_book))
del phone_book['Max']
print(phone_book)
phone_book.update({'Mike': 5468848, 'Bob': 9418686484})
print(phone_book)
print(phone_book.get('Mike'))
print(phone_book.get('Alex', 'Key is not exists'))
bob = phone_book.pop('Bob')
print(phone_book)
print(bob)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())

# homework module_1_6.py
my_dict = {'Lane': 1986, 'Mike': 1980, 'Bob': 2000}
print('Dict:', my_dict)
print('Existing value:', my_dict['Mike'])
print('Not existing value:', my_dict.get('John'))
my_dict.update({'John': 1988, 'Alex': 2001})
print('Deleted value:', my_dict.pop('Mike'))
print('Modified dictionary:', my_dict)