import tkinter as tk

def orig():
    c1 = canvas.create_oval(50, 50, 175, 175, fill="dark grey")
    c2 = canvas.create_oval(50, 220, 175, 345, fill="dark grey")
    c3 = canvas.create_oval(50, 390, 175, 515, fill="dark grey")
    # print(c2, type(c2))

def next_traffic(event):
    global phases, idx
    orig()

    phase = phases[idx]
    rc = phase[0]
    if rc:
        canvas.create_oval(50, 50, 175, 175, fill="red")
    yc = phase[1]
    if yc:
        canvas.create_oval(50, 220, 175, 345, fill="yellow")
    gc = phase[2]
    if gc:
        canvas.create_oval(50, 390, 175, 515, fill="green")

    idx += 1
    idx = idx % len(phases)


window = tk.Tk()
window.title("Traffic Lights")

phases = ((True, False, False),
          (True, True, False),
          (False, False, True),
          (False, True, False))

idx = 0


# canvas = tk.Canvas(window, width=600, height=200, bg="dim grey")
canvas = tk.Canvas(window, width=200, height=600, bg="dim grey")

# c1 = canvas.create_oval(50, 50, 175, 175, fill="dark grey")
# c2 = canvas.create_oval(220, 50, 345, 175, fill="dark grey")
# c3 = canvas.create_oval(390, 50, 515, 175, fill="dark grey")

orig()


btn1 = tk.Button(window, text="Next")
btn1.bind("<Button-1>", next_traffic)
btn2 = tk.Button(window, text="Quit", command=window.destroy)


canvas.grid(row=0)
btn1.grid(row=1)
btn2.grid(row=2)

window.mainloop()