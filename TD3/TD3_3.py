import tkinter as tk
import random


def draw_circle():  # A function that will create a circle with random parameters
    x_center = random.randint(50, 250)
    y_center = random.randint(50, 250)
    radius = random.randint(10, 40)
    color = canvas_color.get()

    canvas.create_oval(x_center - radius, y_center - radius, x_center + radius, y_center + radius,
                       outline=color, width=2)


def change_color():  # Function for changing the color of the circle
    color = colors[random.randint(0, len(colors)-1)]
    canvas.itemconfig("all", outline=color)


def clear_canvas():  # Function that deletes all circles and resets the color to blue
    canvas.delete("all")


root = tk.Tk()  # Creating the main window
root.title("Circle Drawer")

# Creation of the canvas
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Creation of the button "Draw a circle"
draw_button = tk.Button(root, text="Draw a circle", command=draw_circle)
draw_button.pack()

# Creation of the button "Change color"
change_color_button = tk.Button(root, text="Change color", command=change_color)
change_color_button.pack()

# Creation of the button "Clear"
clear_button = tk.Button(root, text="Clear", command=clear_canvas)
clear_button.pack()

# List of possible colors
colors = ['purple', 'cyan', 'green', 'red', 'blue', 'orange', 'black']

# Variable that remembers the color
canvas_color = tk.StringVar()
canvas_color.set('blue')

# The main Tkinter loop
root.mainloop()
