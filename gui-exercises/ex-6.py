import tkinter as tk
from decimal import Decimal


def parse_expression():
    global text, op_rand, op_rator
    expr = text.get()
    opo = ''
    for c in expr:
        if c.isdigit():
            opo += c
        elif c == '.':
            opo += c
        else:
            op_rand.append(c)
            op_rator.append(opo)
            opo = ''
    op_rator.append(opo)

def type_convert(operator):
    if '.' in operator:
        return Decimal(operator)
    return int(operator)


def evaluate(event=None):
    global op_rand, op_rator, text
    parse_expression()

    print(f'oprtor: {op_rator}')
    print(f'oprnd: {op_rand}')

    op1 = op_rator.pop()
    op2 = op_rator.pop()
    oprnd = op_rand.pop()

    if oprnd == '+':
        vsum = type_convert(op1) + type_convert(op2)
        op_rator.append(vsum)
    elif oprnd == '-':
        vsub = type_convert(op2) - type_convert(op1)
        op_rator.append(vsub)
    elif oprnd == '*':
        vmul = type_convert(op1) * type_convert(op2)
        op_rator.append(vmul)
    else:
        if op1 == '0':
            text.set("Error!")
            return
        vdiv = type_convert(op2)/type_convert(op1)
        op_rator.append(vdiv)

    res = str(op_rator.pop())
    if '.' in res:
        if res[res.index('.')+1:] == '0':
            res = res[:len(res)-2]
    text.set(res[:10])

def w_observer(id, ix, act):
    print(f'id: {id}, ix: {ix}, act: {act}')


def calc_input(event=None):
    global operations, op_rand, op_rator
    val = event.widget.cget("text")
    # if val in operations:
    #     op_rand.append(val)
    # if val.isdigit():
    #     op_rator.append(val)

    text.set(text.get() + val)

def clear_screen(event=None):
    text.set("")


window = tk.Tk()
window.title("Calculator")

text = tk.StringVar()


entry = tk.Entry(window, textvariable=text, width=27, font=("Arial", "15", "bold"))
text.set("")
w_obsid = text.trace("w", w_observer)
entry.grid(row=0, columnspan=5)

op_rator = []
op_rand = []


cal_vals = [['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0', 'C', '.']]

for i in range(4):
    for j in range(3):
        btn = tk.Button(window, text=f'{cal_vals[i][j]}', width=5, height=3)
        if i == 3 and j == 1:
            btn.bind("<Button-1>", clear_screen)
        else:
            btn.bind('<Button-1>', calc_input)
        btn.grid(row=i+1, column=j)

ev_btn = tk.Button(window, text="=", width=6, height=3)
ev_btn.bind("<Button-1>", evaluate)
ev_btn.grid(row=3, column=3)
sign_btn = tk.Button(window, text="+/-", width=6, height=3)
sign_btn.bind("<Button-1>", calc_input)
sign_btn.grid(row=4, column=3)

operations = ['+', '-', '*', '/']

for i in range(4):
    btn = tk.Button(window, text=f'{operations[i]}', width=5, height=3)
    btn.bind("<Button-1>", calc_input)
    btn.grid(row=i+1, column=4)


window.mainloop()