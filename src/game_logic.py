import curses
from copy import deepcopy
from typing import Tuple

from src.exceptions import GameOver
from src.tetris_board import TetrisBoard
from src.tetromino import Tetromino


USER_ACTION_TO_TETROMINO_TRANSFORMATION_MAP = {
    "a": "move_left",
    "d": "move_right",
    "w": "rotate_clockwise",
    "s": "rotate_counterclockwise",
}


def start_game(screen: curses.window) -> None:
    curses.echo()  # Echo user input, so it is visible.

    tetris_board = TetrisBoard()
    tetromino = Tetromino.create_random_tetromino(tetris_board.cols_num)
    extra_info_for_user = ""

    while True:
        screen.clear()
        tetris_board.display_with_tetromino(screen, tetromino)

        if tetris_board.no_valid_move_exists_for_tetromino(tetromino):
            new_tetromino = Tetromino.create_random_tetromino(tetris_board.cols_num)
            if tetris_board.no_valid_move_exists_for_tetromino(new_tetromino):
                raise GameOver()
            else:
                tetris_board.save_new_state(tetromino)
                tetromino = new_tetromino
                continue

        user_action = _get_action_from_user(
            screen=screen,
            prompt_display_row=tetris_board.rows_num + 1,
            extra_info_for_user=extra_info_for_user,
        )
        try:
            updated_tetromino, extra_info_for_user = _get_updated_tetromino(
                user_action, tetris_board, tetromino
            )
            if updated_tetromino is not None:
                tetromino = updated_tetromino
        except KeyError:
            extra_info_for_user = f'Action "{user_action}" is invalid.'


def _get_action_from_user(
    screen: curses.window, prompt_display_row: int, extra_info_for_user: str = ""
) -> str:
    prompt_rows = [
        "Write a character representing one of the valid actions below and press ENTER.",
        "  a - to move piece left",
        "  d - to move piece right",
        "  w - to rotate piece counter-clockwise",
        "  s - to rotate piece clockwise",
        "",
        "",  # Here curses will display user input prompt.
        "",
        "  " + extra_info_for_user,
    ]
    prompt_display_col = 0
    for row_index, row in enumerate(prompt_rows):
        screen.addstr(prompt_display_row + row_index, prompt_display_col, row)

    user_input = screen.getstr(prompt_display_row + 6, prompt_display_col + 2, 1).decode().lower()
    return user_input


def _get_updated_tetromino(
    user_action: str, tetris_board: TetrisBoard, tetromino: Tetromino
) -> Tuple[Tetromino, str]:
    extra_info_for_user = ""
    updated_tetromino = None
    tetromino_transformation = USER_ACTION_TO_TETROMINO_TRANSFORMATION_MAP[user_action]

    tetromino_copy = deepcopy(tetromino)
    getattr(tetromino_copy, tetromino_transformation)()

    if tetris_board.is_tetromino_displayable(tetromino_copy):
        updated_tetromino = tetromino_copy
    else:
        extra_info_for_user = f'Action "{user_action}" is invalid in this situation.'
    return updated_tetromino, extra_info_for_user
