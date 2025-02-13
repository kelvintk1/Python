class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    def available_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        Text = current_question.text
        user_answer = input(f"Q{self.question_number}: {Text}. (True / False):\n")
        Answer = current_question.answer
        self.check_answer(user_answer, Answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!\n")
        else:
            print("That's wrong!\n")
        print(f"The correct answer is {correct_answer}.\nYour score is {self.score}/{self.question_number}")
