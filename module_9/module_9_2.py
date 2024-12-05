# Домашнее задание по теме "Списковые, словарные сборки"

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(elem) for elem in first_strings if len(elem) >= 5]
second_result = [(f_elem, s_elem) for f_elem in first_strings for s_elem in second_strings if
                 len(f_elem) == len(s_elem)]
third_result = {elem: len(elem) for elem in first_strings + second_strings if not len(elem) % 2}

print(first_result)
print(second_result)
print(third_result)
