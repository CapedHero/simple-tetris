import curses
from copy import deepcopy
from typing import Iterator, Tuple

from src.tetromino import Tetromino


class TetrisBoard:
    """
    Creates a Tetris board in the shape of rows_num x cols_num.

    For instance, TetrisBoard(rows_num=4, cols_num=6) will create:

    * * * * * *
    *         *
    *         *
    * * * * * *

    Bear in mind that all methods except for save_new_state work on deep copies,
    which makes all tests, validations, etc. safer.
    """

    def __init__(self, rows_num: int = 20, cols_num: int = 20) -> None:
        self.board = []
        self.rows_num = rows_num
        self.cols_num = cols_num

        for row_index in range(self.rows_num):
            if row_index in {0, self.rows_num - 1}:
                row = ["*"] * self.cols_num
            else:
                row = ["*"] + [" "] * (self.cols_num - 2) + ["*"]
            self.board.append(row)

    def display_with_tetromino(self, screen: curses.window, tetromino: Tetromino) -> None:
        display_board = deepcopy(self.board)

        for board_row, board_col in self._yield_tetromino_cell_coordinates(tetromino):
            display_board[board_row][board_col] = "*"

        for row_index, row in enumerate(display_board):
            screen.addstr(row_index, 0, " ".join(row))

    def is_tetromino_displayable(self, tetromino: Tetromino) -> bool:
        display_board = deepcopy(self.board)

        for board_row, board_col in self._yield_tetromino_cell_coordinates(tetromino):
            is_board_cell_already_occupied = display_board[board_row][board_col] == "*"
            if is_board_cell_already_occupied:
                return False

        return True

    def no_valid_move_exists_for_tetromino(self, tetromino: Tetromino) -> bool:
        for tetromino_transformation in [
            "move_left",
            "move_right",
            "rotate_clockwise",
            "rotate_counterclockwise",
        ]:
            tetromino_copy = deepcopy(tetromino)
            getattr(tetromino_copy, tetromino_transformation)()
            if self.is_tetromino_displayable(tetromino_copy):
                return False

        return True

    def save_new_state(self, tetromino: Tetromino) -> None:
        for board_row, board_col in self._yield_tetromino_cell_coordinates(tetromino):
            self.board[board_row][board_col] = "*"

    def _yield_tetromino_cell_coordinates(self, tetromino: Tetromino) -> Iterator[Tuple[int, int]]:
        for offset_row in range(tetromino.drawing_area_size):
            for offset_col in range(tetromino.drawing_area_size):
                is_tetromino_cell = tetromino.shape[offset_row][offset_col] == 1
                if is_tetromino_cell:
                    board_row = tetromino.anchor_row + offset_row
                    board_col = tetromino.anchor_col + offset_col
                    yield board_row, board_col
