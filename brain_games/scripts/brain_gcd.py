from brain_games.games.gcd import generate_question
from brain_games.engine import play_game

def main():
    DESCRIPT = "Find the greatest common divisor of given numbers."
    play_game(DESCRIPT, generate_question)

if __name__ == "__main__":
    main()

