import random

DESCRIPT = "What is the result of the expression?"


def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(["+", "-", "*"])
    question = f"{a} {op} {b}"
    correct_answer = str(eval(question))
    return question, correct_answer
