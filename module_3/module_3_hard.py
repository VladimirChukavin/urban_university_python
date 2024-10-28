# Дополнительное практическое задание по модулю*


def calculate_structure_sum(*args):
    total = 0

    for i in args:
        if isinstance(i, int):
            total += i
        if isinstance(i, str):
            total += len(i)
        if isinstance(i, list):
            total += calculate_structure_sum(*i)
        if isinstance(i, dict):
            dict_to_list = list(i.keys()) + list(i.values())
            total += calculate_structure_sum(*dict_to_list)
        if isinstance(i, tuple):
            tuple_to_list = list(i)
            total += calculate_structure_sum(*tuple_to_list)
        if isinstance(i, set):
            set_to_list = list(i)
            total += calculate_structure_sum(*set_to_list)

    return total


data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)
