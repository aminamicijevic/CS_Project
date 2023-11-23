import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data


def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_buttons[choice].cget("text")

    # Checking if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Updating the score and displaying it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!")
    else:
        feedback_label.config(text="Inorrect!")

    # Disabling all choice buttons and enabling the next button
    for but in choice_buttons:
        but.config(state="disabled")
    next_button.config(state="normal")


def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # If there are more questions, show them
        show_question()
    else:
        # If all questions have been answered, show the final score
        messagebox.showinfo("Quiz Completed!", "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()


def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Displaying the choices on the buttons
    choices = question["choices"]
    for j in range(4):
        choice_buttons[j].config(text=choices[j], state="normal")

    # Clearing the feedback label and disabling the next button
    feedback_label.config(text="")
    next_button.config(state="disabled")


# Creating the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Creating the question label
qs_label = ttk.Label(root, anchor="center", wraplength=500, padding=10)
qs_label.pack(pady=10)

# Creating the choice buttons
choice_buttons = []
for k in range(4):
    button = ttk.Button(root, command=lambda k=k: check_answer(k))
    button.pack(pady=5)
    choice_buttons.append(button)

# Creating the feedback label
feedback_label = ttk.Label(root, anchor="center", padding=10)
feedback_label.pack(pady=10)

# Initializing the score
score = 0

# Creating the score label
score_label = ttk.Label(root, text="Score: 0/{}".format(len(quiz_data)), anchor="center", padding=10)
score_label.pack(pady=10)

# Creating the next button
next_button = ttk.Button(root, text="Next", command=next_question, state="disabled")
next_button.pack(pady=10)

# Initializing the current question index
current_question = 0

# Showing the first question
show_question()

# Starting the main loop
root.mainloop()
