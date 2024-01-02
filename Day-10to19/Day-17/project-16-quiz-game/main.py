from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for qa_pair in question_data:
    text = qa_pair["question"]
    answer = qa_pair["correct_answer"]
    new_q = Question(text,answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() :
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")