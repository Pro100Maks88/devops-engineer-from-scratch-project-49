import random
from brain_games.games.start_end import END_RANDOM, START_RANDOM

def generate_question():
    assert START_RANDOM <= END_RANDOM, "START_RANDOM должен быть <= END_RANDOM"

    a = random.randint(START_RANDOM, END_RANDOM)
    b = random.randint(START_RANDOM, END_RANDOM)

    
    if a == 0 and b == 0:
        return generate_question()

    original_a, original_b = a, b
    question = f"Найдите НОД чисел {original_a} и {original_b}"

    while a != 0 and b != 0:
        a, b = b, a % b
    correct_answer = a if a != 0 else b

    return question, str(correct_answer)

