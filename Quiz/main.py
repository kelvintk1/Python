from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question.text)
    question_bank.append(new_question.answer)

quiz = QuizBrain(question_bank)
while quiz.available_questions():
    quiz.next_question()
