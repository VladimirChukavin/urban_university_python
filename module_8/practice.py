# Практика-исключения

def calc(data_string):
    operation_list = ['+', '-', '*', '/', '//', '%']
    num_1, operation, num_2 = data_string.replace('\n', '').split(' ')
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operation in operation_list and operation == '+':
        print(f'Result: {num_1 + num_2}')
    if operation in operation_list and operation == '-':
        print(f'Result: {num_1 - num_2}')
    if operation in operation_list and operation == '*':
        print(f'Result: {num_1 * num_2}')
    if operation in operation_list and operation == '/':
        print(f'Result: {num_1 / num_2}')
    if operation in operation_list and operation == '//':
        print(f'Result: {num_1 // num_2}')
    if operation in operation_list and operation == '%':
        print(f'Result: {num_1 % num_2}')


count = 0
error_list = []

with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        count += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                # print(f'Error in line {count}, not enough values to unpack')
                error_list.append(f'Error in line {count}, not enough values to unpack')
            else:
                # print(f'Error in line {count}, invalid literal for convert to integer')
                error_list.append(f'Error in line {count}, invalid literal for convert to integer')

print(*error_list, sep='\n')
