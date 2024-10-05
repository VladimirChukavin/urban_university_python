# Условная конструкция. Операторы if, elif, else

# name = input("Enter your name: ")
# if name == 'urban':
#     print('Hello, admin')
# if name == 'test':
#     print('Hi, user')
# else:
#     print('Welcome', name)

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 5 == 0:
    print('Buzz')
elif number % 3 == 0:
    print('Fizz')
else:
    print('Incorrect number')
