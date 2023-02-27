import tkinter as tk
import data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class TriviaUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.trivia = quiz_brain
        self.window = tk.Tk()
        self.window.title("Trivia")
        self.window.config(padx=20, pady=20, background=THEME_COLOR, width=400, height=500)
        self.score = tk.Label(text=f"Score: {self.trivia.score}", fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.question_area = tk.Canvas(width=300, height=250, bg='white')
        self.question_area.grid(row=1, column=0, pady=50, columnspan=2)
        self.question = self.question_area.create_text(150, 125, text=f"Question here", width=280,
                                                       font=("Arial", 20, 'italic'), fill=THEME_COLOR)
        true_img = tk.PhotoImage(file="images/true.png")
        # self.right_button = tk.Button(image=true_img, borderwidth=0, highlightthickness=0,
        #                               command=lambda: self.trivia.check_answer("True"))
        self.right_button = tk.Button(image=true_img, borderwidth=0, highlightthickness=0,
                                      command=self.true_pressed)
        self.right_button.grid(row=2, column=0)
        false_img = tk.PhotoImage(file="images/false.png")
        # self.wrong_button = tk.Button(image=false_img, borderwidth=0, highlightthickness=0,
        #                               command=lambda: self.trivia.check_answer("False"))
        self.wrong_button = tk.Button(image=false_img, borderwidth=0, highlightthickness=0,
                                      command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_area.config(bg='white')

        if self.trivia.still_has_questions():
            self.score.config(text=f"Score: {self.trivia.score}")
            q_text = self.trivia.next_question()
            self.question_area.itemconfig(self.question, text=q_text)
        else:
            self.question_area.itemconfig(text="You have reached the end of the Trivia Game!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.trivia.check_answer("True"))
        # # the above basically does below
        # is_right = self.trivia.check_answer("True")
        # self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.trivia.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.question_area.config(bg='green')
            # self.window.after(3000,self.question_area.config(bg='green'))
            self.question_area.after(1000, self.get_next_question)
        else:
            # self.window.after(1000, func=lambda: self.question_area.config(bg='red'))
            self.question_area.config(bg='red')
            # self.window.after(3000)
            # self.get_next_question()
            self.question_area.after(1000, self.get_next_question)
