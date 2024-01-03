import tkinter as tk
from tkinter import ttk
from NormalMode import NormalMode
from TimedMode import TimedMode
from MillionaireMode import MillionaireMode
from FlashcardMode import FlashcardMode

class QuizApp:
    def __init__(self, rootinit):
        # Initialize the main Quiz App window
        self.root = rootinit
        self.root.title("Medical Sensors Quiz")
        self.root.geometry("360x640")
        self.root.configure(bg="#ADD8E6")

        # Configure styles for widgets
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Roboto", 16), background="#ADD8E6", anchor="center", padding=(10, 5))
        self.style.configure("TButton", font=("Roboto", 14), padding=10, anchor="center")
        self.style.configure("Question.TFrame", background="#ADD8E6", padx=10, pady=15, width=360)

        # Initialize variables
        self.quiz_mode = "Normal Mode"
        self.num_questions = 10

        # Create and display widgets
        self.create_widgets()

    def create_widgets(self):
        # Create the title frame
        self.title_frame = tk.Frame(self.root, bg="#ADD8E6")
        self.title_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Create and display the title label
        self.title_label = tk.Label(self.title_frame, text="M e d i c a l\nS e n s o r s\nQ u i z", font=("Courier", 22),
                                    bg="#ADD8E6")
        self.title_label.pack(side="top", pady=(10, 20))

        # Define options for buttons
        button_options = {"fill": "x", "padx": 10, "pady": 10, "side": "top"}

        # Create and display buttons
        self.quiz_mode_button = tk.Button(self.root, text="Quiz Mode", command=self.open_quiz_mode, font=("Roboto", 14))
        self.quiz_mode_button.pack(**button_options)

        self.question_sets_button = tk.Button(self.root, text="Question Sets", command=self.open_question_sets,
                                              font=("Roboto", 14))
        self.question_sets_button.pack(**button_options)

        self.num_questions_button = tk.Button(self.root, text="Number of Questions", command=self.open_num_questions,
                                              font=("Roboto", 14))
        self.num_questions_button.pack(**button_options)

        self.start_quiz_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz, font=("Roboto", 14))
        self.start_quiz_button.pack(**button_options)

    def open_quiz_mode(self):
        # Open the window to select quiz mode
        quiz_mode_window = tk.Toplevel(self.root)
        quiz_mode_window.title("Quiz Mode")
        quiz_mode_window.geometry("360x640")
        quiz_mode_window.configure(bg="#ADD8E6")

        # Display the label for selecting quiz mode
        label = tk.Label(quiz_mode_window, text="Select Quiz Mode:", font=("Roboto", 14, "bold"), bg="#ADD8E6")
        label.pack(pady=10)

        # Create and display check buttons for quiz modes
        quiz_mode_var = tk.StringVar()
        quiz_mode_var.set(self.quiz_mode)
        modes = ["Normal Mode", "Timed Mode", "Millionaire Mode", "Flashcard Mode"]
        for mode in modes:
            check_button = tk.Checkbutton(quiz_mode_window, text=mode, variable=quiz_mode_var, onvalue=mode, offvalue="",
                                          font=("Roboto", 14), bg="#ADD8E6")
            check_button.pack()

        # Display the OK button to confirm the selected mode
        confirm_button = tk.Button(quiz_mode_window, text="OK",
                                   command=lambda: self.set_quiz_mode(quiz_mode_var.get(), quiz_mode_window),
                                   font=("Roboto", 14))
        confirm_button.pack(pady=10)

    def set_quiz_mode(self, mode, window):
        # Set the selected quiz mode and close the window
        self.quiz_mode = mode
        window.destroy()

    def open_question_sets(self):
        # TODO: Implement opening the window for selecting question sets
        pass

    def open_num_questions(self):
        # Open the window to select the number of questions
        num_questions_window = tk.Toplevel(self.root)
        num_questions_window.title("Number of Questions")
        num_questions_window.geometry("360x640")
        num_questions_window.configure(bg="#ADD8E6")

        # Display the label for selecting the number of questions
        label = tk.Label(num_questions_window, text="Select Number of Questions:", font=("Roboto", 14, "bold"),
                         bg="#ADD8E6")
        label.pack(pady=10)

        # Create and display check buttons for the number of questions
        num_questions_var = tk.IntVar()
        num_questions_var.set(self.num_questions)
        for num in [10, 20, 25, 50]:
            check_button = tk.Checkbutton(num_questions_window, text=str(num), variable=num_questions_var, onvalue=num,
                                          offvalue=0, font=("Roboto", 14), bg="#ADD8E6")
            check_button.pack()

        # Display the OK button to confirm the selected number of questions
        confirm_button = tk.Button(num_questions_window, text="OK",
                                   command=lambda: self.set_num_questions(num_questions_var.get(), num_questions_window),
                                   font=("Roboto", 14))
        confirm_button.pack(pady=10)

    def set_num_questions(self, value, window):
        # Set the selected number of questions and close the window
        self.num_questions = value
        window.destroy()

    def start_quiz(self):
        # Start the selected quiz mode
        if self.quiz_mode == "Normal Mode":
            self.start_normal_mode()
        elif self.quiz_mode == "Timed Mode":
            self.start_timed_mode()
        elif self.quiz_mode == "Millionaire Mode":
            self.start_millionaire_mode()
        elif self.quiz_mode == "Flashcard Mode":
            self.start_flashcard_mode()

    def start_normal_mode(self):
        # Start the Normal Mode quiz
        normal_mode_window = tk.Toplevel(self.root)
        normal_mode_app = NormalMode(normal_mode_window, num_questions=self.num_questions)

    def start_timed_mode(self):
        # Start the Timed Mode quiz
        timed_mode_window = tk.Toplevel(self.root)
        timed_mode_app = TimedMode(timed_mode_window, num_questions=self.num_questions)

    def start_millionaire_mode(self):
        # Start the Millionaire Mode quiz
        millionaire_mode_window = tk.Toplevel(self.root)
        millionaire_mode_app = MillionaireMode(millionaire_mode_window)

    def start_flashcard_mode(self):
        # Start the Flashcard Mode quiz
        flashcard_mode_window = tk.Toplevel(self.root)
        flashcard_mode_app = FlashcardMode(flashcard_mode_window)

if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
