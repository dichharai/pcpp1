import tkinter as tk
from tkinter import messagebox

def display_winner(message):
    messagebox.showinfo("Game Over!", message)

def check_diagonal_wins(pos_list, who):
    print('in digonal')
    
    di0 = [f'({i}, {i})' for i in range(3)]
    di1 = [f'({i}, {2-i})' for i in range(2, -1, -1)]

    if all([el in di0 for el in pos_list]) or all([el in di1 for el in pos_list]):
        if who == 'r':
            display_winner("Computer won!")
        else:
            display_winner("I won!")


def check_vertical_wins(pos_list, who):
    col0 = [f'({i}, 0)' for i in range(3)]
    col1 = [f'({i}, 1)' for i in range(3)]
    col2 = [f'({i}, 2)' for i in range(3)]

    if all([el in pos_list for el in col0]) or all([el in pos_list for el in col1]) or all([el in pos_list for el in col2]):
        if who == 'r':
            display_winner("Computer won!")
        else:
            display_winner("I won!")


def check_horizontal_wins(pos_list, who):
    row0 = [f'(0, {i})' for i in range(3)]
    row1 = [f'(1, {i})' for i in range(3)]
    row2 = [f'(2, {i})' for i in range(3)]

    if all([el in pos_list for el in row0]) or all([el in pos_list for el in row1]) or all([el in pos_list for el in row2]):
        if who == 'r':
            display_winner("Computer won!")
        else:
            display_winner("I won!")



def tic_tac_toe(event):
    global reds, greens, switch
    if not switch:
        event.widget.config(text="O", foreground="green")
        greens.append(event.widget._pos)
        print(f'g: {greens}')
        
        if len(greens) >= 3:
            print('in greens')
            check_vertical_wins(greens, "g")
            check_horizontal_wins(greens, "g")
            check_diagonal_wins(greens, "g")
    else:
        event.widget.config(text="X", foreground="red")
        reds.append(event.widget._pos)
        print(f'r: {reds}')
        if len(reds) >= 3:
            print("in greens")
            check_vertical_wins(reds, "r")
            check_horizontal_wins(reds, "r")
            check_diagonal_wins(reds, "r")
    

    # event.widget.after(100, None)
    switch = not switch
    
        
window = tk.Tk()
window.title("TicTacToe")

greens = []
reds = []

switch = False
for i in range(3):
    for j in range(3):
        var = tk.StringVar()
        btn = tk.Button(window, width=7, height=4, borderwidth=0, border=3)
        btn._pos = f'({i}, {j})'
        if i == 1 and j == 1:
            btn.config(text='X', foreground="red")
            reds.append(btn._pos)
        
        btn.bind("<Button-1>", tic_tac_toe)
        btn.grid(row=i, column=j)

window.mainloop()