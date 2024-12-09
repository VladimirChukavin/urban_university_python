# Домашнее задание по теме "Генераторы"
from itertools import combinations


def all_variants(text):
    for item in range(1, len(text) + 1):
        list_text = list(''.join(el) for el in combinations(text, item))
        for el in list_text:
            yield el


a = all_variants("abc")

for i in a:
    print(i)
