# Функции практика 1.2 (Калькулятор)
# Функции практика 1.3 (Калькулятор-финал)


import tkinter as tk


def get_values():
    num_one = int(entry_one.get())
    num_two = int(entry_two.get())
    return num_one, num_two


def insert_value(value):
    result.delete(0, "end")
    result.insert(0, str(value))


def add():
    num_1, num_2 = get_values()
    res = num_1 + num_2
    insert_value(res)


def sub():
    num_1, num_2 = get_values()
    res = num_1 - num_2
    insert_value(res)


def mul():
    num_1, num_2 = get_values()
    res = num_1 * num_2
    insert_value(res)


def div():
    num_1, num_2 = get_values()
    res = num_1 / num_2
    insert_value(res)


window = tk.Tk()
window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)

button_add = tk.Button(window, text="+", width=2, height=2, command=add)
button_add.place(x=75, y=250)

button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=125, y=250)

button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=175, y=250)

button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=225, y=250)

entry_one = tk.Entry(window, width=23)
entry_one.place(x=75, y=75)
label_one = tk.Label(window, text="Введите первое число:")
label_one.place(x=75, y=50)

entry_two = tk.Entry(window, width=23)
entry_two.place(x=75, y=130)
label_two = tk.Label(window, text="Введите второе число:")
label_two.place(x=75, y=105)

result = tk.Entry(window, width=23)
result.place(x=75, y=185)
label_result = tk.Label(window, text="Результат:")
label_result.place(x=75, y=160)

window.mainloop()
