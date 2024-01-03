import tkinter as tk
from tkinter import ttk
from quiz_data import quiz_data

class FlashcardMode:
    def __init__(self, root):
        # Initialize the Flashcard Mode
        self.root = root
        self.root.title("Flashcard Mode")
        self.root.geometry("360x320")
        self.root.configure(bg="white")

        # Configure styles for widgets
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Roboto", 16), background="white", anchor="center", padding=(10, 5))
        self.style.configure("TButton", font=("Roboto", 14), padding=10, anchor="center", background="#ADD8E6")
        self.style.configure("Flashcard.TFrame", background="white", padx=10, pady=15, width=400)

        # Initialize variables
        self.current_question = 0
        self.showing_answer = False  # Flag to track whether the answer is currently displayed

        # Create and display widgets
        self.create_widgets()
        self.show_flashcard()

    def create_widgets(self):
        # Create the flashcard frame
        self.flashcard_frame = ttk.Frame(self.root, style="Flashcard.TFrame")
        self.flashcard_frame.pack(fill="both", expand=True)

        # Create the flashcard label
        self.flashcard_label = tk.Label(self.flashcard_frame, text="", font=("Roboto", 16), wraplength=380,
                                        justify="center", bg="white")
        self.flashcard_label.pack(fill="both", expand=True)

        # Create the toggle button
        self.toggle_button = tk.Button(self.root, text="Show Answer", command=self.toggle_show_answer,
                                       font=("Roboto", 14), width=20, bg="#ADD8E6")
        self.toggle_button.pack(pady=10)

        # Create the next flashcard button
        self.next_flashcard_button = tk.Button(self.root, text="Next Flashcard", command=self.next_flashcard,
                                               font=("Roboto", 14), width=20, bg="#ADD8E6")
        self.next_flashcard_button.pack(pady=10)

        # Create the restart button
        self.restart_button = tk.Button(self.root, text="Restart Set", command=self.restart_set,
                                        font=("Roboto", 14), width=20, bg="#ADD8E6")

    def show_flashcard(self):
        # Display the current flashcard content
        if self.showing_answer:
            answer = quiz_data[self.current_question]["answer"]
            flashcard_text = f"{answer}"
            self.toggle_button.config(text="Show Question")
        else:
            question = quiz_data[self.current_question]["question"]
            flashcard_text = f"{question}"
            self.toggle_button.config(text="Show Answer")

        self.flashcard_label.config(text=flashcard_text)

    def toggle_show_answer(self):
        # Toggle between showing question and answer
        self.showing_answer = not self.showing_answer
        self.show_flashcard()

    def next_flashcard(self):
        # Move to the next flashcard
        self.current_question += 1
        self.showing_answer = False  # Reset to show question by default
        if self.current_question < len(quiz_data):
            self.show_flashcard()
        else:
            self.hide_buttons()
            self.flashcard_label.config(text="No more flashcards!")

            if self.current_question >= len(quiz_data):
                self.restart_button.pack(pady=10)

    def hide_buttons(self):
        # Hide toggle and next buttons
        self.toggle_button.pack_forget()
        self.next_flashcard_button.pack_forget()

    def restart_set(self):
        # Restart the flashcard set
        self.current_question = 0
        self.showing_answer = False
        self.show_flashcard()
        self.show_buttons()

    def show_buttons(self):
        # Show toggle and next buttons
        self.toggle_button.pack(pady=10)
        self.next_flashcard_button.pack(pady=10)
        self.restart_button.pack_forget()  # Initially hidden

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardMode(root)
    app.show_buttons()  # Initially show toggle and next buttons
    root.mainloop()
