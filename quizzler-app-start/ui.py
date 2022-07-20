import quiz_brain

THEME_COLOR = "#576F72"
FONT = ("Arial", 20, "italic")

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 120, width=280,text="question", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1,columnspan=2, pady=50)


        # scoreboard label
        self.score_label = Label(text=f"score: 0", font=FONT)
        self.score_label.config(bg=THEME_COLOR, fg="white",pady=20, padx=20)
        self.score_label.grid(column=1, row=0)


        # button
        self.false_button_img = PhotoImage(file="images/false.png")
        self.true_button_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=self.false_button_img, command=self.click_false)
        self.false_button.config(bg=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(column=1, row=2)
        self.true_button = Button(image=self.true_button_img, command=self.click_true)
        self.true_button.config(bg=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Congrats! You've finished all the questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def click_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def click_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)












