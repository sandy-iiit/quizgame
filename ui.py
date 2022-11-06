from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#E97777"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain) -> None:
        self.quiz = quizbrain
        self.window = Tk();
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(150, 125, width=290, text="Some qqq", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2)

        self.trueimg = PhotoImage(file="images/true.png")
        self.tbutton = Button(image=self.trueimg, highlightthickness=0, command=self.true_pressed)
        self.tbutton.grid(row=2, column=0)

        self.fimg = PhotoImage(file="images/false.png")
        self.fbutton = Button(image=self.fimg, highlightthickness=0, command=self.false_pressed)
        self.fbutton.grid(row=2, column=1)

        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            qtext = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=qtext)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz...")
            self.tbutton.config(state="disabled")
            self.fbutton.config(state="disabled")

    def true_pressed(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        answer = self.quiz.check_answer("False")
        self.get_feedback(answer)

    def get_feedback(self, ans):
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_q)
