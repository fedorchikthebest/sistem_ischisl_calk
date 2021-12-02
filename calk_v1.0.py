from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


def clicked():
    try:
        a = int(txt.get())
        b = ''
        c = 0
        if combo.get() == 'Двоичная':
            while a != 0:
                b += str(a % 2)
                a //= 2
                c += 1
                if c == 4:
                    b += ' '
                    c = 0
            messagebox.showinfo('Ответ от Фёдора:', b[::-1])

        if combo.get() == 'Восьмиричня':
            while a > 0:
                b += str(a % 8)
                a //= 8
                c += 1
                if c == 3:
                    b += ' '
                    c = 0
            messagebox.showinfo('Ответ от Фёдора:', b[::-1])

        if combo.get() == 'Шестнадацатиричная':
            d = ['A', 'B', 'C', 'D', 'E', 'F']
            while a > 0:
                if a % 16 < 10:
                    b += str(a % 16)
                else:
                    b += d[a % 16 - 10]
                a //= 16
                c += 1
                if c == 3:
                    b += ' '
                    c = 0
            messagebox.showinfo('Ответ от Фёдора:', b[::-1])

    except ValueError:
        messagebox.showinfo('Ошибка!!!', 'Вы ввели не число!')


window = Tk()
window.title("Системы исчисления")
window.geometry('325x50')

lbl = Label(window, text="Введите число:", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

lbl1 = Label(window, text="Выберете систему:", font=("Arial Bold", 10))
lbl1.grid(column=1, row=0)

combo = Combobox(window, width=18)
combo['values'] = ('Двоичная', 'Восьмиричня', 'Шестнадацатиричная')
combo.current(0)
combo.grid(column=1, row=1)

txt = Entry(window, width=20)
txt.grid(column=0, row=1)

btn = Button(window, text="Вычислить", command=clicked)
btn.grid(column=2, row=1)

window.mainloop()