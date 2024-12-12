# Практика

animal = 'bear'
animals = ['dog', 'cat', 'rabit']


def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal

    return repeat


test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animal))

print('-' * 40)

repeats = [gen_repeat(n) for n in range(1, 4)]
print(repeats)

result = [func(animal) for func in repeats]
print(result)

print('-' * 40)

fin_result = [func(x) for func in repeats for x in animals]
print(fin_result)

print('-' * 40)


def memoize_func(f):
    memo = {}

    def wrapper(*args):
        if args not in memo:
            memo[args] = f(*args)
            return f'Function called, result = {memo[args]}, {memo}'
        else:
            return f'Function execute, result from memory = {memo[args]}'

    return wrapper

@memoize_func
def func_pow(a, b):
    print(f'Call function with arguments ({a}, {b})')
    return a ** b


print(func_pow(3, 5), end='\n')
print(func_pow(3, 4), end='\n')
print(func_pow(3, 2), end='\n')
print(func_pow(3, 5), end='\n')
print(func_pow(3, 4), end='\n')
print(func_pow(3, 5), end='\n')
