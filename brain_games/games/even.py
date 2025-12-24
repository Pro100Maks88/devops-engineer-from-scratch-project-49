import random

from brain_games.games.start_end import START_RANDOM, END_RANDOM

def generate_question():
    n = random.randint(START_RANDOM, END_RANDOM)
    return n, "yes" if n % 2 == 0 else "no"
