import tkinter as tk
from datetime import datetime


def display_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=f"Current Time: {current_time}")


root = tk.Tk()  # Creating the main window
root.title("Current Time Display")

# Creating the label for showing the current time
time_label = tk.Label(root, text=f"", font=("Times New Roman", 12))
time_label.pack()

# Creating the button that the user will press
time_button = tk.Button(root, text="Current Time", command=display_current_time)
time_button.pack()

# The main Tkinter loop
root.mainloop()
