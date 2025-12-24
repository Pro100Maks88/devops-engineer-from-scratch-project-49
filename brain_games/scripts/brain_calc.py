from brain_games.engine import play_game
from brain_games.games.calc import DESCRIPT, generate_question


def main():
    play_game(DESCRIPT, generate_question)


if __name__ == "__main__":
    main()
