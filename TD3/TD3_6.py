import tkinter as tk
import math

# Gravitational constant
G = 6.67430e-11

# Masses of the stars
star1_mass = 10000
star2_mass = 1000

# The starting coordinates
star1_x, star1_y = 200, 150
star2_x, star2_y = 300, 150


def calculate_distance(x1, y1, x2, y2):  # Function used to calculate distance between the stars
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def calculate_gravitational_force(m1, m2, r):  # Function that calculates the gravitational force
    return (G * m1 * m2) / (r**2)


def update_info():  # A function that updates the distance and force
    distance = calculate_distance(star1_x, star1_y, star2_x, star2_y)
    force = calculate_gravitational_force(star1_mass, star2_mass, distance)
    info_label.config(text=f"Distance: {distance} m\nGravitational Force: {force} N")
    mass_label.config(text=f"Star 1 Mass: {star1_mass} kg\nStar 2 Mass: {star2_mass} kg")


def move_star1(dx, dy):  # A function that moves star 1
    global star1_x, star1_y
    star1_x += dx
    star1_y += dy
    canvas.coords(star1, star1_x-10, star1_y-10, star1_x+10, star1_y+10)
    update_info()


def move_star2(dx, dy):  # A function that moves star 2
    global star2_x, star2_y
    star2_x += dx
    star2_y += dy
    canvas.coords(star2, star2_x-5, star2_y-5, star2_x+5, star2_y+5)
    update_info()


root = tk.Tk()  # Creating the main window
root.title("Stars and Gravity")

# Creating a canvas to draw stars
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# Creating stars
star1 = canvas.create_oval(star1_x-10, star1_y-10, star1_x+10, star1_y+10, outline='pink', fill='pink')
star2 = canvas.create_oval(star2_x-5, star2_y-5, star2_x+5, star2_y+5, outline='purple', fill='purple')

# Buttons for moving stars
move_star1_button = tk.Button(root, text="Move Star 1", command=lambda: move_star1(10, 0))
move_star1_button.pack()
move_star2_button = tk.Button(root, text="Move Star 2", command=lambda: move_star2(10, 0))
move_star2_button.pack()

# Information label
info_label = tk.Label(root, text="", justify="left")
info_label.pack()

# Mass label
mass_label = tk.Label(root, text="", justify="left")
mass_label.pack()

# Initializing the information display
update_info()

# The main Tkinter loop
root.mainloop()
