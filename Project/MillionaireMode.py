import tkinter as tk
from tkinter import ttk
import random
from quiz_data import quiz_data


class MillionaireMode:
    def __init__(self, rootinit, chosen_set):
        # Initialize the Quiz App
        self.root = rootinit
        self.root.title("Quiz App")
        self.root.geometry("360x640")
        self.root.configure(bg="white")

        # Configure styles for widgets
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Roboto", 16), background="white", anchor="center", padding=(10, 5))
        self.style.configure("TButton", font=("Roboto", 14), padding=10, anchor="center")
        self.style.configure("Question.TFrame", background="white", padx=10, pady=15, width=360)

        # Initialize quiz parameters
        self.current_question = 0
        self.score = 0
        self.money = 0
        self.game_over = False
        self.correct_answer = False
        self.chosen_set = chosen_set

        # Filter questions based on the chosen set
        self.qs_for_set = [question for question in quiz_data if question["set_id"] in self.chosen_set]

        # Create and display widgets
        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        # Create the main frame and configure its appearance
        self.white_frame = tk.Frame(self.root, bg="white", bd=1, relief="solid", padx=1, pady=1)
        self.white_frame.pack(side="top", fill="x", padx=10, pady=(5, 0))

        # Frame to display the current question
        self.question_frame = ttk.Frame(self.root, style="Question.TFrame")
        self.question_frame.pack(pady=20, fill="both", expand=True)

        # Frame to hold the question label
        self.qs_label_frame = ttk.Frame(self.question_frame, style="Question.TFrame")
        self.qs_label_frame.pack(fill="both", expand=True)

        # Label to display the question
        self.qs_label = tk.Label(self.qs_label_frame, wraplength=320, font=("Roboto", 16), bg="white", anchor="center")
        self.qs_label.pack(fill="both", expand=True)

        # Create choice buttons
        self.choice_buttons = []
        for k in range(4):
            button = tk.Button(self.root, command=lambda k=k: self.check_answer(k), font=("Roboto", 14), wraplength=300)
            button.pack(pady=8, fill="both", padx=10)
            self.choice_buttons.append(button)

        # Label to provide feedback on the user's answer
        self.feedback_label = tk.Label(self.root, font=("Roboto", 14), bg="white", padx=10, pady=5)
        self.feedback_label.pack(pady=5)

        # Button to move to the next question
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Roboto", 14))
        self.next_button.pack(pady=10)
        self.next_button.config(state="disabled")

        # Label to display the money earned
        self.money_label = tk.Label(self.white_frame, text="Money: ${}".format(self.money),
                                    font=("Roboto", 14), bg="white", anchor="center")
        self.money_label.pack(side="top", pady=1)

    def show_question(self):
        # Display the next question
        if self.game_over:
            return

        random.shuffle(self.qs_for_set)
        question = self.qs_for_set[0]

        self.qs_label.config(text=question["question"], justify="center", anchor="center")

        choices = question["choices"]
        for j in range(4):
            self.choice_buttons[j].config(text=choices[j], state="normal", background="SystemButtonFace", wraplength=300)

        self.next_button.config(state="disabled")
        self.correct_answer = False

    def check_answer(self, choice):
        # Check the selected answer against the correct answer
        if self.game_over:
            return

        question = self.qs_for_set[0]
        self.qs_for_set.pop(0)

        selected_choice = self.choice_buttons[choice].cget("text")

        if selected_choice == question["answer"]:
            correct_choice_index = question["choices"].index(question["answer"])
            self.choice_buttons[correct_choice_index].config(background="#98FB98")
            self.choice_buttons[choice].config(background="#98FB98")
            self.score += 1
            self.money = self.calculate_money()
            self.money_label.config(text="Money: ${}".format(self.money))
            self.show_feedback("Correct! You won ${}!".format(self.money))
            self.correct_answer = True
            self.next_button.config(state="normal")
        else:
            correct_choice_index = question["choices"].index(question["answer"])
            self.choice_buttons[correct_choice_index].config(background="#98FB98")
            self.choice_buttons[choice].config(background="#E57373")
            self.show_feedback("Incorrect! Game over. You earned ${}".format(0))
            self.game_over = True
            self.next_button.config(state="disabled")

        for button in self.choice_buttons:
            button.config(state="disabled")

    def show_feedback(self, feedback):
        # Display feedback message
        self.feedback_label.config(text=feedback, fg="#008000")

    def next_question(self):
        # Move to the next question or end the quiz
        self.current_question += 1

        if self.current_question < len(quiz_data):
            self.game_over = False
            self.show_question()
            self.feedback_label.config(text="")
            self.next_button.config(state="disabled")
        else:
            final_result = "Quiz Completed! Money Earned: ${}".format(self.money)
            self.show_feedback(final_result)
            self.next_button.config(state="disabled")

    def calculate_money(self):
        # Calculate money earned based on the current question
        money_values = [50, 100, 250, 500, 1000, 2000, 4000, 8000, 16000,
                        32000, 64000, 125000, 250000, 500000, 1000000]

        if self.current_question < len(money_values):
            return money_values[self.current_question]
        else:
            return 0

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = MillionaireMode(root)
    root.mainloop()
