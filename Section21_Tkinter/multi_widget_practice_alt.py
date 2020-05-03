#! python3
# Alternate import

import tkinter as tk

window = tk.Tk()


def kg_to_g_lb_oz():
    t1.delete(1.0, tk.END)
    t2.delete(1.0, tk.END)
    t3.delete(1.0, tk.END)
    kg = float(e1_value.get())
    g = kg * 1000
    lb = kg * 2.20462
    oz = kg * 35.274
    t1.insert(tk.END, g)
    t2.insert(tk.END, lb)
    t3.insert(tk.END, oz)


b1 = tk.Button(window, text='Convert', command=kg_to_g_lb_oz)
b1.grid(row=0, column=2)

e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

w1 = tk.Label(window, text='kg')
w1.grid(row=0, column=0)

t1 = tk.Text(height=1, width=20)
t1.grid(row=1, column=0)
t2 = tk.Text(height=1, width=20)
t2.grid(row=1, column=1)
t3 = tk.Text(height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
