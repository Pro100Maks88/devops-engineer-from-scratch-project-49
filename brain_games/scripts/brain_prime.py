from brain_games.engine import play_game
from brain_games.games.prime import generate_question


def main():
    DESCRIPT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play_game(DESCRIPT, generate_question)


if __name__ == "__main__":
    main()
