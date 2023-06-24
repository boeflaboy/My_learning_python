from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question = questions['text']
    answer = questions['answer']
    question_bank.append(Question(question, answer))

questions = QuizBrain(question_bank)
question_number = 1
while True:

    user_input = input(f'Q.{question_number}: {question_bank[questions.question_number].text} (True/False): ').title()

    if questions.check_question(user_input, question_bank[questions.question_number].answer):
        print("You got it correct")
        if questions.check_end_of_question_list():
            print("There are no more questions")
            break
        questions.question_number = questions.next_question()
        question_number += 1
    else:
        print("You are wrong")



