from brain_games.games.cli import welcome_user

ROUNDS = 3


def play_game(DESCRIPT, module_with_game):
    name = welcome_user()
    print(DESCRIPT)
    for _ in range(ROUNDS):
        question, correct_answer = module_with_game.generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    else:
        print(f"Congratulations, {name}!")