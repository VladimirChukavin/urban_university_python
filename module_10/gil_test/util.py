import datetime
import json
from random import randint

res = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']
time_calc = []


# for file in files:
#     for _ in range(100000):
#         res.append(randint(1, 10000))
#     with open(file, 'w', encoding='utf-8') as f:
#         json.dump(res, f, indent=4)
#     res = []

def main():
    res_to_count = []
    start = datetime.datetime.now()

    for file in files:
        with open(file, 'r') as f:
            data = json.load(f)
            res_to_count.extend(data)
    sum(res_to_count)
    end = datetime.datetime.now()
    return end - start


for i in range(100):
    res = []
    time_calc.append(main())

print(sum([calc.microseconds for calc in time_calc]) / len(time_calc))
# 30141.11