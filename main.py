import curses
import sys

from src.exceptions import GameOver
from src.game_logic import start_game


if __name__ == "__main__":
    try:
        curses.wrapper(start_game)
    except KeyboardInterrupt:
        print()
        print("Game stopped by the player.")
        sys.exit(0)
    except GameOver:
        print()
        print("No valid moves left.")
        print()
        print("Game Over")
        sys.exit(0)
