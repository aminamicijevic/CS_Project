import tkinter as tk

# Dictionary to store the drawn rings
drawn_rings = {}


def draw_olympic_ring(canv, col, x, y):
    x_center, y_center = x, y
    ring_radius = 40
    canv.create_oval(x_center - ring_radius, y_center - ring_radius, x_center + ring_radius, y_center + ring_radius,
                     outline=col, width=2)


def set_selected_color(col, x, y):
    global selected_color
    selected_color = col
    draw_olympic_ring(canvas, col, x, y)
    drawn_rings[col] = (x, y)


root = tk.Tk()  # Creating the main window
root.title("Olympic Rings")

# Creating a canvas to draw on
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# Creating a "Quit" button to close the window
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

# Predefined coordinates for each ring
ring_coordinates = [(150, 125), (250, 125), (350, 125), (200, 175), (300, 175)]
color_names = ['Blue', 'Black', 'Red', 'Yellow', 'Green']

# Creating buttons to select ring colors
for i, color in enumerate(color_names):
    button = tk.Button(root, text=color, command=lambda c=color.lower(), x=ring_coordinates[i][0], y=ring_coordinates[i][1]: set_selected_color(c, x, y))
    button.pack(side=tk.LEFT)

# The main Tkinter loop
root.mainloop()
