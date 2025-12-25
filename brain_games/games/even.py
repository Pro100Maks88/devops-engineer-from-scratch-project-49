DESCRIPT = "Answer 'yes' if the number is even, otherwise answer 'no'."

import random


def generate_question():

    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer


if __name__ == "__main__":
    from brain_games.engine import play_game
    play_game(__name__)







