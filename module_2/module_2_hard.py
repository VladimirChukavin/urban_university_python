# Дополнительное практическое задание по модулю
import random

number = random.randint(3, 20)


def decoding(n):
    num_list = [i for i in range(1, n)]

    res_list = []

    for i in range(len(num_list) // 2):
        for j in range(i + 1, len(num_list)):
            if n % (num_list[i] + num_list[j]) == 0:
                res_list.append(f'{num_list[i]}{num_list[j]}')

    result = ''.join(res_list)
    return result


print(f'{number} -', decoding(number))
