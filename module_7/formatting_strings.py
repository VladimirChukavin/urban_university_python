# Форматирование строк

print('Hello, ' + 'world' + str(13))
print('I am %s, i is %s' % ('John', 'programmer'))
print('I am %(name)s, old %(year)s' % {'name': 'John', 'year': 2022})
print('This is {} {}'.format('Urban', 'university'))
print('This is {0}-{1} {0}'.format('Urban', 'university'))
print('This is {title}-{postfix}'.format(title='Urban', postfix='university'))
print(f'{'Urban' * 2} the best')