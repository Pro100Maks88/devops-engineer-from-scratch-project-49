DESCRIPT = "What number is missing in the progression?"

import random


def generate_progression():
    
    start = random.randint(1, 20)
    
    step = random.randint(1, 5)
    
    length = random.randint(6, 10)
    
    progression = [start + i * step for i in range(length)]
    
    hidden_index = random.randint(1, length - 2)
    correct_answer = progression[hidden_index]
    
    progression[hidden_index] = '..'
    
    return progression, str(correct_answer)


def generate_question():
    progression, correct_answer = generate_progression()
    question = ' '.join(map(str, progression))
    return question, correct_answer

