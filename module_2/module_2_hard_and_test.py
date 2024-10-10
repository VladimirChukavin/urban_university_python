# Дополнительное практическое задание по модулю

def decoding(n):
    num_list = [i for i in range(1, n)]

    res_list = []

    for i in range(len(num_list) // 2):
        for j in range(i + 1, len(num_list)):
            if n % (num_list[i] + num_list[j]) == 0:
                res_list.append(f'{num_list[i]}{num_list[j]}')

    result = ''.join(res_list)
    return result


test_input = [i for i in range(3, 21)]
test_result = ['12', '13', '1423', '121524', '162534', '13172635', '1218273645', '141923283746', '11029384756',
               '12131511124210394857', '112211310495867', '1611325212343114105968', '1214114232133124115106978',
               '1317115262143531341251161079', '11621531441351261171089', '12151811724272163631545414513612711810',
               '118217316415514613712811910', '13141911923282183731746416515614713812911']

for i in test_input:
    print(test_result[i - 3], decoding(i), decoding(i) in test_result)
