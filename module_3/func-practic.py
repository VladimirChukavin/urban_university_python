# Практика по функциям


def find_max(list_):
    max_num = list_[0]

    for i in list_:
        if i > max_num:
            max_num = i

    return max_num


print(find_max([1, 33, 7, 93, 0, -25]))
print(find_max([1, 33, 7, 0, -25]))


def count_even(list_):
    counter = 0

    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1

    return counter


print(count_even([2, 3, 4, 9, 8, 36, 0]))


def unique(list_):
    new_list = []

    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(unique([1, 2, 2, 3, 4, 5, 5]))


def unique_alt(list_):
    return list(set(list_))


print(unique_alt([1, 2, 3, 4, 5, 5]))
