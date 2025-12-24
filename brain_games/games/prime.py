import random

from brain_games.games.start_end import END_RANDOM, START_RANDOM


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def generate_question():
    number = random.randint(START_RANDOM, END_RANDOM)

    if is_prime(number):
        return number, "yes"
    else:
        return number, "no"
