import random
from brain_games.games.start_end import END_RANDOM, START_RANDOM

def generate_question():

    a = random.randint(START_RANDOM, END_RANDOM)
    b = random.randint(START_RANDOM, END_RANDOM)

    question = f"{a} {b}"
    
    while a != 0 and b != 0:
        a, b = b, a % b
    
    correct_answer = a if a != 0 else b
    return question, str(correct_answer)
