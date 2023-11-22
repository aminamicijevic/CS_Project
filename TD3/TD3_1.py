import tkinter as tk


def display_result():  # Function that will be called when user presses the button Display
    last_name = last_name_entry.get()
    first_name = first_name_entry.get()
    date_of_birth = date_of_birth_entry.get()

    result_label.config(text=f"{last_name} {first_name} was born on {date_of_birth}.")


root = tk.Tk()  # Creating the main window
root.title("User Information")

# Creating the labels and entry fields for all data
last_name_label = tk.Label(root, text="Last Name: ")
last_name_label.pack()

last_name_entry = tk.Entry(root)
last_name_entry.pack()

first_name_label = tk.Label(root, text="First Name: ")
first_name_label.pack()

first_name_entry = tk.Entry(root)
first_name_entry.pack()

date_of_birth_label = tk.Label(root, text="Date of Birth: ")
date_of_birth_label.pack()

date_of_birth_entry = tk.Entry(root)
date_of_birth_entry.pack()

# Creating the button that will display all user info
submit_button = tk.Button(root, text="Display", command=display_result)
submit_button.pack()

# Creating a label to display the result
result_label = tk.Label(root, text="", font=("Times New Roman", 12))
result_label.pack()

# The main Tkinter loop
root.mainloop()
