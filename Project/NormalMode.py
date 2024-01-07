import tkinter as tk
from tkinter import ttk
import random
from quiz_data import quiz_data


class NormalMode:
    def __init__(self, rootinit, num_questions, chosen_set):
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
        self.num_questions = num_questions
        self.current_question = 0
        self.score = 0
        self.chosen_set = chosen_set

        # Filter questions based on the chosen set
        self.qs_for_set = [question for question in quiz_data if question["set_id"] in self.chosen_set]

        # Create and display widgets
        self.create_widgets()

        # Display the first question
        self.show_question()

    def create_widgets(self):
        # Create the main frame and configure its appearance
        self.white_frame = tk.Frame(self.root, bg="white", bd=1, relief="solid", padx=1, pady=1)
        self.white_frame.pack(side="top", fill="x", padx=10, pady=(5, 0))

        # Create a canvas to display progress bar
        self.canvas_width = 285
        self.canvas_height = 10
        self.canvas = tk.Canvas(self.white_frame, width=self.canvas_width, height=self.canvas_height, bg="white",
                                bd=0, highlightthickness=0)
        self.canvas.pack(side="left", padx=1, pady=1)

        # Label to display current question number
        self.question_number_label = tk.Label(self.white_frame, text="1/{}".format(self.num_questions),
                                              font=("Roboto", 12), bg="white", anchor="e", padx=10)
        self.question_number_label.pack(side="right", pady=1)

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
        self.feedback_label = tk.Label(self.root, font=("Roboto", 14), bg="white", padx=10, pady=5, wraplength=340)
        self.feedback_label.pack(pady=5)

        # Button to move to the next question
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Roboto", 14))
        self.next_button.pack(pady=10)

    def show_question(self):
        # Shuffle the quiz data to get a random order of questions
        random.shuffle(self.qs_for_set)
        question = self.qs_for_set[0]
        self.qs_label.config(text=question["question"], justify="center", anchor="center")

        # Display choices for the current question
        choices = question["choices"]
        random.shuffle(choices)
        for j in range(4):
            self.choice_buttons[j].config(text=choices[j], state="normal", background="#ADD8E6")

        # Reset feedback label and enable the next button
        self.feedback_label.config(text="")
        self.next_button.config(state="disabled")

        # Update the progress bar
        self.canvas.delete("all")
        fill_color = "#ADD8E6"
        sivi_fill_color = "#D3D3D3"
        x0, y0, x1, y1 = (5, (10 - self.canvas_height) / 2, 10 + self.canvas_width * (self.current_question + 1) /
                          self.num_questions, 10 - (10 - self.canvas_height) / 2)
        x1_sivi = x0 + self.canvas_width
        self.canvas.create_rectangle(x0, y0, x1_sivi, y1, fill=sivi_fill_color, outline="")
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color, outline="")
        self.canvas.tag_raise("all")

        # Update the question number label
        self.question_number_label.config(text="{}/{}".format(self.current_question + 1, self.num_questions))

    def check_answer(self, choice):
        # Check the selected answer against the correct answer
        question = self.qs_for_set[0]
        self.qs_for_set.pop(0)
        selected_choice = self.choice_buttons[choice].cget("text")

        # Disable all choice buttons
        for button in self.choice_buttons:
            button.config(state="disabled")

        # Provide feedback based on correctness
        if selected_choice == question["answer"]:
            self.choice_buttons[choice].config(background="#98FB98")
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="#008000")
        else:
            correct_choice_index = question["choices"].index(question["answer"])
            self.choice_buttons[choice].config(background="#E57373")
            self.choice_buttons[correct_choice_index].config(background="#98FB98")
            self.feedback_label.config(text="Incorrect!", fg="#FF0000")

        # Enable the next button
        self.next_button.config(state="normal")

    def next_question(self):
        # Move to the next question or end the quiz
        self.current_question += 1
        if self.current_question < self.num_questions and len(self.qs_for_set) > 0:
            self.show_question()
        else:
            final_result = "Quiz Completed! Final score: {}/{}".format(self.score, self.current_question)
            self.feedback_label.config(text=final_result, fg="#008000")
            self.next_button.config(state="disabled")


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    num_questions = 10
    app = NormalMode(root, num_questions)
    root.mainloop()
