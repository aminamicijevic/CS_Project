import tkinter as tk
from tkinter import ttk


def change_bg_color(event):  # Function for changing the color of the main window
    selected_color = combo_var.get()

    if selected_color.lower() in [color.lower() for color in colors]:
        # If the color is not on the list
        root.configure(background=selected_color)
    else:
        root.configure(background=selected_color)


root = tk.Tk()  # Creating the main window
root.title("ComboBox")

# Creation of the ComboBox widget
combo_var = tk.StringVar()
colors = ['white', 'red', 'green', 'blue', 'yellow', 'pink', 'purple']
combo = ttk.Combobox(root, textvariable=combo_var, values=colors)
combo.pack(padx=20, pady=10)

# Setting the default color to white
combo_var.set('white')

# Binding of the ComboBox and the function for changing the color (list)
combo.bind('<<ComboboxSelected>>', change_bg_color)

# Binding of the ComboBox and the function for changing the color (entering the name)
combo.bind("<Return>", change_bg_color)

# Creating a label with the selected color
color_label = tk.Label(root, text="Selected Color: ")
color_label.pack()

# Creating a button that will show the selected color
show_color_button = tk.Button(root, text="Show Selected Color",
                              command=lambda: color_label.config(text=f"Selected Color: {combo_var.get()}"))
show_color_button.pack()

# The main Tkinter loop
root.mainloop()
