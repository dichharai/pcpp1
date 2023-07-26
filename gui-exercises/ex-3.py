import tkinter as tk
import random

window = tk.Tk()
window.title("Clicker")

def increment_label():
    global count
    count += 1
    time_label.config(text=count)
    if count < 25:
        time_label.after(1000, increment_label)


def num_check(event):
    global idx, nums
    print(nums[idx])
    # print(event, dir(event))
    print(event.widget.cget("text"))
    if event.widget.cget("text") == str(nums[idx]):
        event.widget.config(state=tk.DISABLED)
        print('yes')
        idx += 1
    else:
        print('nope')



count = 0
idx = 0
nums = []
unique = False
for i in range(5):
    for j in range(5):
        value = 0
        while not unique:
            num = random.randrange(1, 1000)
            if num not in nums:
                nums.append(num)
                value = num
                unique = True

        btn = tk.Button(window, text=f'{num}', borderwidth=4, width=8)
        btn.bind("<Button-1>", num_check)
        btn.grid(row=i, column=j)
        unique = False

nums = sorted(nums)
time_label = tk.Label(window, text=count)
tl_id = time_label.after(1000, increment_label)
time_label.grid(columnspan=5)
print(tl_id)



window.mainloop()