# Домашнее задание по теме "Обзор сторонних библиотек Python"

import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3, c='tomato')

ax.set_title('График квадратичной функции', fontsize=24)
ax.set_xlabel('Аргумент', fontsize=14)
ax.set_ylabel('Квадрат аргумента', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 110, 0, 11000])

plt.show()
# plt.savefig('squares_plot.png')
