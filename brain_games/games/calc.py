import random

from brain_games.games.start_end import END_RANDOM, START_RANDOM

OPERATORS = ("+", "-", "*")

def generate_question():
    number1 = random.randint(START_RANDOM, END_RANDOM)
    number2 = random.randint(START_RANDOM, END_RANDOM)
    operator = random.choice(OPERATORS)
    
    question = f"{number1} {operator} {number2}"
    correct_answer = calc(number1, number2, operator)
    
    return question, str(correct_answer)

def calc(number1, number2, operator):
    
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2