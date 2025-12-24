from brain_games.games.calc import generate_question
from brain_games.engine import play_game

def main():
    DESCRIPT = "What is the result of the expression?"
    play_game(DESCRIPT, generate_question)

if __name__ == "__main__":
    main()
