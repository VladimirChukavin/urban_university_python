# Крестики-нолики

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


def draw_area():
    for i in area:
        print('|', *i, '|')
    print()


def check_win(combination):
    win_list = [[0, 0, 0, 0, 1, 2], [0, 1, 1, 1, 1, 2], [0, 1, 2, 2, 2, 2], [0, 0, 1, 1, 2, 2]]

    if combination in win_list:
        return True


# test = [0, 2, 1, 2, 2, 2]
# print(check_win(sorted(test)))

print('Крестики-нолики')
print('-' * 16)
draw_area()


def tic_tac():
    cross_combination = []
    zero_combination = []

    for turn in range(1, 10):
        print(f'Ход: {turn}')
        if turn % 2 == 0:
            turn_char = '0'
            print('Ход Нолик')
        else:
            turn_char = 'X'
            print('Ход Крестик')

        while True:
            row = int(input('Введите номер строки (1, 2, 3): ')) - 1
            column = int(input('Введите номер столбца (1, 2, 3): ')) - 1
            if 0 <= row < 3 and 0 <= column < 3:
                break

        if area[row][column] == '*':
            area[row][column] = turn_char
        else:
            print('Ячейка занята, пропуск хода')
            draw_area()
            continue

        if turn_char == 'X':
            cross_combination.extend([row, column])
        if turn_char == '0':
            zero_combination.extend([row, column])

        draw_area()

        if check_win(sorted(cross_combination)):
            print('Победа Крестик')
            break
        if check_win(sorted(zero_combination)):
            print('Победа Нолик')
            break
        if not check_win(sorted(cross_combination)) and turn == 9:
            print('Ничья')
            break


tic_tac()
