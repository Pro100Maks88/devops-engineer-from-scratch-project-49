DESCRIPT = "Answer 'yes' if the number is prime, otherwise answer 'no'."

import random

def is_prime(n):

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_question():
    number = random.randint(2, 50)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer

