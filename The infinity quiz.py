import tkinter as tk
from tkinter import ttk

# Model
class QuizModel:
    def __init__(self):
        self.questions = [
            {"question": "What is the output of 'print(8 // 3)' in Python?", "answers": ["2.67", "2", "3", "2.6666"], "correct": 1},
            {"question": "How do you insert COMMENTS in Python code?", "answers": ["/* comment */", "// comment", "# comment", "<!-- comment -->"], "correct": 2},
            {"question": "Which operator is used in Python to check if two values are the same?", "answers": ["=", "==", "equals", "==="], "correct": 1},
            {"question": "What does the 'len()' function in Python return?", "answers": ["The length of a string", "The size of an object", "The character at a specific index", "The number of keys in a dictionary"], "correct": 0},
            {"question": "How is a list defined in Python?", "answers": ["[]", "{}", "()", "<>"], "correct": 0},
            {"question": "What is a correct syntax to return the first character in a string named 'str'?", "answers": ["str[1]", "str(0)", "str[0]", "str.first()"], "correct": 2},
            {"question": "Which method can be used to return a string in upper case letters?", "answers": [".uppercase()", ".upper()", ".toUpperCase()", ".upCase()"], "correct": 1},
            {"question": "How do you start writing a function in Python?", "answers": ["function myFunction():", "def myFunction():", "create myFunction():", "function: myFunction()"], "correct": 1},
            {"question": "What is the correct file extension for Python files?", "answers": [".pyth", ".pt", ".py", ".python"], "correct": 2},
            {"question": "How do you create a variable with the floating number 2.8 in Python?", "answers": ["x = float(2.8)", "float x = 2.8", "x = 2.8", "x = float:2.8"], "correct": 2},
            {"question": "Did you have fun", "answers": ["Yes","credit song for my death but im the final boss.","Potat","Demonic Wrath"], "correct": 0}
        ]

    def get_question(self, index):
        return self.questions[index]


# Quiz View
class QuizView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.selected_answer = tk.IntVar(value=-1)

        # Score Label
        self.score_var = tk.StringVar(value="Score: 0")                                        # This will hold the score text
        self.score_label = tk.Label(self, textvariable=self.score_var, font=("Arial", 12))     # The label that shows the score
        self.score_label.pack(anchor='ne', padx=10, pady=10)                                   # Put the score label in the top right corner

        # Question Label
        self.question_label = tk.Label(self, text="", font=("Arial", 14))                      # The label for the question text
        self.question_label.pack(pady=(10, 20))                                                # Put the question label in the window

        self.buttons_frame = tk.Frame(self)                                                    # A frame to hold the answer buttons
        self.buttons_frame.pack(pady=10)                                                       # Put the frame in the window

        self.answer_radio_buttons = []                                                         # A list to keep all the answer buttons
        for i in range(4):                                                                     # Make 4 answer buttons
            radio_btn = ttk.Radiobutton(self.buttons_frame, text="", variable=self.selected_answer, value=i)  # Create a radio button
            radio_btn.grid(row=i//2, column=i%2, pady=5, padx=10)                              # Put the button in the grid
            self.answer_radio_buttons.append(radio_btn)                                        # Add the button to our list

        # Submit Button
        self.submit_button = ttk.Button(self, text="Submit", command=self.controller.submit_answer)  # The button to submit your answer
        self.submit_button.pack(pady=10)                                                       # Put the submit button in the window

    def set_question(self, question):
        self.question_label.config(text=question["question"])                                  # Set the question text
        self.selected_answer.set(-1)                                                           # Reset the selected answer to none
        for i, radio_btn in enumerate(self.answer_radio_buttons):
            radio_btn.config(text=question["answers"][i])                                      # Set the text for each answer button

    def update_score(self, new_score):
        self.score_var.set(f"Score: {new_score}")                                              # Update the score label with the new score

    def show_temporary_message(self, message):
        temp_label = tk.Label(self, text=message, font=("Arial", 12), fg="red")                # Create a temporary message label
        temp_label.pack(pady=5)                                                                # Show the label
        self.after(1000, temp_label.destroy)                                                   # Remove the label after 1 second

    def show_final_score(self, score):
        self.show_temporary_message(f"Your Score is {score}")                                  # Show the final score







class QuizController:
    def __init__(self, model, view):
        self.model = model  # Save the model
        self.view = view  # Save the view
        self.current_question_index = 0  # Start at the first question
        self.score = 0  # Start the score at 0
        if self.view:
            self.display_question()  # Show the first question if the view is set

    def display_question(self):
        if self.current_question_index < len(self.model.questions):  # Check if there are more questions
            question = self.model.get_question(self.current_question_index)  # Get the next question
            self.view.set_question(question)  # Display the question in the view

    def submit_answer(self):
        selected_index = self.view.selected_answer.get()  # Get the selected answer
        if selected_index != -1:  # Check if an answer is selected
            correct_index = self.model.get_question(self.current_question_index)["correct"]  # Get the correct answer
            if selected_index == correct_index:  # Check if the selected answer is correct
                self.score += 1  # Increase the score
                self.view.show_temporary_message("Correct!")  # Show a correct message
            else:
                self.view.show_temporary_message("Incorrect.")  # Show an incorrect message
            self.view.update_score(self.score)  # Update the score in the view
            self.current_question_index += 1  # Go to the next question
            self.view.after(1000, self.display_question)  # Wait 1 second and show the next question
        else:
            self.view.show_temporary_message("Please select an answer.")  # Ask to select an answer



# Main
if __name__ == "__main__":
    model = QuizModel()  # Create the quiz model
    controller = QuizController(model, None)  # Create the quiz controller
    view = QuizView(controller)  # Create the quiz view
    controller.view = view  # Set the view in the controller
    controller.display_question()  # Start the quiz
    view.mainloop()  # Run the tkinter loop
