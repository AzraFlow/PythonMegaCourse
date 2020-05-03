#! python3 branch code

from tkinter import *

window = Tk()


def kg_to_g_lb_oz():
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    kg = float(e1_value.get())
    g = kg * 1000
    lb = kg * 2.20462
    oz = kg * 35.274
    t1.insert(END, g)
    t2.insert(END, lb)
    t3.insert(END, oz)


b1 = Button(window, text='Convert', command=kg_to_g_lb_oz)
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

w1 = Label(window, text='kg')
w1.grid(row=0, column=0)

t1 = Text(height=1, width=20)
t1.grid(row=1, column=0)
t2 = Text(height=1, width=20)
t2.grid(row=1, column=1)
t3 = Text(height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
