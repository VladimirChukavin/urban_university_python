# Практика. 1.1
# Практика. 1.2 Итоги модуля

import os
import tkinter
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = text['text'] + ' ' + filename
    os.startfile(filename)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.resizable(False, False)
window.configure(background='grey')

text = tkinter.Label(window, text='Файл:', width=64, height=5, background='lightblue', foreground='tomato')
text.grid(column=1, row=1)

button_select = tkinter.Button(window, width=20, height=2, text='Выбрать файл', background='white',
                               foreground='tomato', command=file_select)
button_select.grid(column=1, row=2, pady=5)

window.mainloop()
