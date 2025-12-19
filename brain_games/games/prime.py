import random

from brain_games.games.start_end import END_RANDOM, START_RANDOM


def generate_question():
    number = random.randint(START_RANDOM, END_RANDOM)
    if number < 2:
        return number, "no"
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return number, "no"
    
    return number, "yes"
