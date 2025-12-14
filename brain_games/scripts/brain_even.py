import random

def welcome_user():

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correctanswers = 0

    while correctanswers < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        your_num = input('Your answer: ').strip().lower()

        correct_answer = 'yes' if random_number % 2 == 0 else 'no'

        if your_num == correct_answer:
            print('Correct!')
            correctanswers += 1
        else:
            print(f"'{your_num}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

def main():

    welcome_user()

if __name__ == "__main__":
    main()










