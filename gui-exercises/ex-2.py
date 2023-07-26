import tkinter as tk
import random

def mouseover(event=None):
    global button
    fx = random.randint(1, 499)
    fy = random.randint(1, 499)
    print(f'ex: {event.x}, ey: {event.y}')
    print(f'fx: {fx}, fy: {fy}')
    button.place(x=fx, y=fy)


window = tk.Tk()
window.title("Catcher")
window.geometry("500x500")


button = tk.Button(window, text="Catch me!", padx=2, pady=2)
button.bind("<Enter>", mouseover)
button.place(x=1, y=2)

window.mainloop()