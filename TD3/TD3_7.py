import tkinter as tk
import math


def calculate():
    expression = entry.get()
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")


def clear():
    entry.delete(0, tk.END)


root = tk.Tk()  # Creating the main window
root.title("Calculator")

# Widget for user input
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')'
]

row_val, col_val = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val,
                                                                                                     column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Square root button
tk.Button(root, text="sqrt", width=5, command=lambda: entry.insert(tk.END, "math.sqrt(")).grid(row=row_val,
                                                                                               column=col_val)
# Clear button
tk.Button(root, text="Clear", width=20, command=clear).grid(row=row_val + 2, columnspan=4)

# The main Tkinter loop
root.mainloop()
