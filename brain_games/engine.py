ROUNDS = 3

def play_game(DESCRIPT, question_generator):
    from brain_games.cli import welcome_user
    name = welcome_user()
    print(DESCRIPT)
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
    
    else:
        print(f"Congratulations, {name}!")
