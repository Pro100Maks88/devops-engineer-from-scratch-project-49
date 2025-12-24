from brain_games.games.calc import generate_question, DESCRIPT
from brain_games.engine import play_game

def main():
    play_game(DESCRIPT, generate_question)

if __name__ == "__main__":
    main()

