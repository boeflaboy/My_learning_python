class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def check_question(self, user_input, question_answer):
        if user_input == question_answer:
            return True
        return False

    def next_question(self):
        self.question_number += 1
        return self.question_number

    def check_end_of_question_list(self):
        if self.question_number == len(self.question_list) - 1:
            return True
        return False




