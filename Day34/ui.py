from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(700, 800)
        self.window.maxsize(700, 800)
        self.window.config(padx=90, pady=50, bg=THEME_COLOR)
        self.scorelabel = Label(text="Score: 0", font=("Arial", 25, "bold"), highlightthickness=0, bg=THEME_COLOR, fg="#ffffff")
        self.scorelabel.grid(column=0, row=0, columnspan=2)
        self.canvas = Canvas(width=500, height=450, bg="#ffffff")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.questiontext = self.canvas.create_text(250, 250, width=480, text="Some Question Text", font=("Arial", 20, "bold"))
        self.phototrue = PhotoImage(file="Day34/images/true.png")
        self.photofalse = PhotoImage(file="Day34/images/false.png")
        self.truebtn = Button(image=self.phototrue, command=self.true_pressed)
        self.truebtn.grid(column=0, row=2)
        self.falsebtn = Button(image=self.photofalse, command=self.false_pressed)
        self.falsebtn.grid(column=1, row=2)
        self.get_next_question()
        self.doinganswer = False
        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.scorelabel.config(text=f"Score: {self.quiz.score}")
            self.doinganswer = False
            self.canvas.itemconfig(self.questiontext, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.questiontext, text="You've reached the end of the quiz")
    
    def true_pressed(self):
        if not self.doinganswer:
            is_right = self.quiz.check_answer("True")
            self.give_feedback(is_right)

    def false_pressed(self):
        if not self.doinganswer:
            is_right = self.quiz.check_answer("False")
            self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.doinganswer = True
        self.window.after(1000, self.get_next_question)