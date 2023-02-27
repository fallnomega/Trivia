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
        self.score = tk.Label(text=f"Score: 0",fg='white',bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.question_area = tk.Canvas(width=300, height=250,bg='white')
        self.question_area.grid(row=1, column=0,pady=50,columnspan=2)
        self.question = self.question_area.create_text(150, 125, text=f"Question here", width=280,
                                             font=("Arial", 20, 'italic'),fill=THEME_COLOR)
        true_img = tk.PhotoImage(file="images/true.png")
        self.right_button = tk.Button(image=true_img,borderwidth=0,highlightthickness=0)
        self.right_button.grid(row=2,column=0)
        false_img = tk.PhotoImage(file="images/false.png")
        self.wrong_button = tk.Button(image=false_img, borderwidth=0,highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.trivia.next_question()
        self.question_area.itemconfig(self.question,text=q_text)