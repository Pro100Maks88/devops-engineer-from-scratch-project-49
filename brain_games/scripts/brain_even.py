from brain_games.engine import play_game
from brain_games.games.even import generate_question


def main():
    DESCRIPT = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(DESCRIPT, generate_question)


if __name__ == "__main__":
    main()
