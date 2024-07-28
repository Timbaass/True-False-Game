from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in range(len(question_data)):
    question = Question(question_data[item]["text"],question_data[item]["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
