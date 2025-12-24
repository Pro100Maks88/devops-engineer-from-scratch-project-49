import random
from brain_games.games.start_end import START_RANDOM, END_RANDOM

START_SIZE_RANDOM = 5

def generate_question():
    start = random.randint(START_RANDOM, END_RANDOM)
    size = random.randint(START_SIZE_RANDOM, END_RANDOM)
    step = random.randint(START_RANDOM, END_RANDOM)
    index_answer = random.randint(0, size)

    progression = [
        ".." if i == index_answer else str(start + i * step)
        for i in range(size + 1)
    ]

    question = " ".join(progression)
    correct_answer = str(start + index_answer * step)

    return question, correct_answer

