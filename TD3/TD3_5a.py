import tkinter as tk


def draw_olympic_rings():  # Function to draw Olympic rings
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 450, 250, outline='black', width=2)

    colors = ['blue', 'black', 'red', 'yellow', 'green']
    ring_coordinates = [(150, 125), (250, 125), (350, 125), (200, 175), (300, 175)]

    for i, color in enumerate(colors):
        x, y = ring_coordinates[i]
        canvas.create_oval(x - 40, y - 40, x + 40, y + 40, outline=color, width=2)


root = tk.Tk()  # Creating the main window
root.title("Olympic Rings")

# Creating a canvas to draw on
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# Creating a "Quit" button to close the window
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

# Drawing all Olympic rings initially
draw_olympic_rings()

# The main Tkinter loop
root.mainloop()
