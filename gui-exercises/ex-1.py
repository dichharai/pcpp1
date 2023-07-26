import tkinter as tk
from tkinter import messagebox

def display(res):
    print(res)
    messagebox.showinfo('Result', f'evaluation result is {res}')

def evaluate():
    global switch
    d1 = int(en1.get())
    d2 = int(en2.get())
    op = switch.get()

    if op == 0:
        display(d1+d2)
    elif op == 1:
        display(d1-d2)
    elif op == 2:
        display(d1*d2)
    elif op == 3:
        if d2 != 0:
            display(d1/d2)
        else:
            messagebox.showinfo('warning', "cannot divide by 0!")
    else:
        messagebox.showinfo("Info", "Not a valid operator")
        

window = tk.Tk()
window.title("Calculator")


switch = tk.IntVar()
switch.set(0)

frame = tk.Frame(window)

radio_btn1 = tk.Radiobutton(frame, text="+", variable=switch, value=0)
radio_btn2 = tk.Radiobutton(frame, text="-", variable=switch, value=1)
radio_btn3 = tk.Radiobutton(frame, text="*", variable=switch, value=2)
radio_btn4 = tk.Radiobutton(frame, text="/", variable=switch, value=3)

radio_btn1.grid(column=0, row=0)
radio_btn2.grid(column=0, row=1)
radio_btn3.grid(column=0, row=2)
radio_btn4.grid(column=0, row=3)

frame.grid(column=1, row=1)

en1 = tk.Entry(window, justify="left", width=20)
en2 = tk.Entry(window, justify="right", width=20)

en1.grid(column=0, row=1)
en2.grid(column=2, row=1)

button = tk.Button(window, text="Evaluate", command=evaluate)
button.grid(column=1, row=4)

window.mainloop()