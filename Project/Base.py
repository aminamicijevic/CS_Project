import tkinter as tk
from tkinter import ttk
from quiz_data import quiz_data


class QuizApp:
    def __init__(self, rootinit):
        # Initialize the QuizApp class with the root window
        self.root = rootinit
        self.root.title("Quiz App")  # Set the title of the window
        self.root.geometry("360x640")  # Set the initial size of the window
        self.root.configure(bg="white")  # Set the background color of the window to white

        # Configure styles for labels, buttons, and the question frame
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Roboto", 16), background="white", anchor="center", padding=(10, 5))
        self.style.configure("TButton", font=("Roboto", 14), padding=10, anchor="center")
        self.style.configure("Question.TFrame", background="white", padx=10, pady=15, width=360)

        self.current_question = 0  # Initialize the current question index
        self.score = 0  # Initialize the score

        # Create GUI elements
        self.create_widgets()

        # Display the first question
        self.show_question()

    def create_widgets(self):
        # Create a white frame at the top of the window
        self.white_frame = tk.Frame(self.root, bg="white", bd=1, relief="solid", padx=1, pady=1)
        self.white_frame.pack(side="top", fill="x", padx=10, pady=(5, 0))

        # Create a canvas to display status
        self.canvas_width = 285
        self.canvas_height = 10
        self.canvas = tk.Canvas(self.white_frame, width=self.canvas_width, height=self.canvas_height, bg="white",
                                bd=0, highlightthickness=0)
        self.canvas.pack(side="left", padx=1, pady=1)

        # Display the current question number
        self.question_number_label = tk.Label(self.white_frame, text="1/{}".format(len(quiz_data)),
                                              font=("Roboto", 12), bg="white", anchor="e", padx=10)
        self.question_number_label.pack(side="right", pady=1)

        # Create a frame for the question
        self.question_frame = ttk.Frame(self.root, style="Question.TFrame")
        self.question_frame.pack(pady=20, fill="both", expand=True)

        # Create a frame for the question label
        self.qs_label_frame = ttk.Frame(self.question_frame, style="Question.TFrame")
        self.qs_label_frame.pack(fill="both", expand=True)

        # Display the question label
        self.qs_label = tk.Label(self.qs_label_frame, wraplength=320, font=("Roboto", 16), bg="white", anchor="center")
        self.qs_label.pack(fill="both", expand=True)

        # Create buttons for answer choices
        self.choice_buttons = []
        for k in range(4):
            button = tk.Button(self.root, command=lambda k=k: self.check_answer(k), font=("Roboto", 14))
            button.pack(pady=8, fill="both", padx=10)
            self.choice_buttons.append(button)

        # Display feedback label
        self.feedback_label = tk.Label(self.root, font=("Roboto", 14), bg="white", padx=10, pady=5)
        self.feedback_label.pack(pady=5)

        # Create the "Next" button
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Roboto", 14))
        self.next_button.pack(pady=10)

    def show_question(self):
        # Display the current question and reset button styles
        question = quiz_data[self.current_question]
        self.qs_label.config(text=question["question"], justify="center", anchor="center")

        choices = question["choices"]
        for j in range(4):
            self.choice_buttons[j].config(text=choices[j], state="normal", background="#ADD8E6")

        self.feedback_label.config(text="")
        self.next_button.config(state="disabled")

        # Clear the canvas
        self.canvas.delete("all")

        fill_color = "#ADD8E6"
        sivi_fill_color = "#D3D3D3"

        # Position and dimensions of the rectangle
        x0, y0, x1, y1 = (5, (10 - self.canvas_height) / 2, 10 + self.canvas_width * (self.current_question + 1) /
                          len(quiz_data), 10 - (10 - self.canvas_height) / 2)

        x1_sivi = x0 + self.canvas_width
        self.canvas.create_rectangle(x0, y0, x1_sivi, y1, fill=sivi_fill_color, outline="")

        self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color, outline="")
        self.canvas.tag_raise("all")

        self.question_number_label.config(text="{}/{}".format(self.current_question + 1, len(quiz_data)))

    def check_answer(self, choice):
        # Check the selected answer and update the UI accordingly
        question = quiz_data[self.current_question]
        selected_choice = self.choice_buttons[choice].cget("text")

        if selected_choice == question["answer"]:
            self.choice_buttons[choice].config(background="#98FB98")
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="#008000")
        else:
            self.choice_buttons[choice].config(background="#E57373")
            self.feedback_label.config(text="Incorrect!", fg="#FF0000")

        # Disable all buttons
        for button in self.choice_buttons:
            button.config(state="disabled")

        # Enable next question button
        self.next_button.config(state="normal")

    def next_question(self):
        # Move to the next question or show the final result if there are no more questions
        self.current_question += 1

        if self.current_question < len(quiz_data):
            self.show_question()
        else:
            final_result = "Quiz Completed! Final score: {}/{}".format(self.score, len(quiz_data))
            self.feedback_label.config(text=final_result, fg="#008000")  # Dark green text
            self.next_button.config(state="disabled")  # Disable the "Next" button


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
