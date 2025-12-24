from brain_games.games.progression import generate_question
from brain_games.engine import play_game

def main():
    DESCRIPT = "What number is missing in the progression?"
    play_game(DESCRIPT, generate_question)

if __name__ == "__main__":
    main()
