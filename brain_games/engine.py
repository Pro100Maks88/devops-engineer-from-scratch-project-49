ROUNDS = 3


def play_game(game_module):
    from brain_games.cli import welcome_user

    description = game_module.DESCRIPT
    question_generator = game_module.generate_question

    name = welcome_user()
    print(description)

    for _ in range(ROUNDS):
        question, correct_answer = question_generator()
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

    print(f"Congratulations, {name}!")