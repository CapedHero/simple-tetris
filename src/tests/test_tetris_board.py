import unittest
from unittest.mock import Mock, call

from src.tetris_board import TetrisBoard
from src.tetromino import Tetromino


class TestTetrisBoard(unittest.TestCase):
    def test_init_logic(self):
        # WHEN
        tetris_board = TetrisBoard(rows_num=4, cols_num=4)

        # THEN
        # fmt: off
        self.assertEqual(tetris_board.board, [
            ["*", "*", "*", "*"],
            ["*", " ", " ", "*"],
            ["*", " ", " ", "*"],
            ["*", "*", "*", "*"],
        ])
        # fmt: on

    def test_display_with_tetromino(self):
        # GIVEN
        mocked_screen = Mock()
        tetris_board = TetrisBoard(rows_num=4, cols_num=4)
        tetromino = Tetromino(drawing_area_size=1, anchor_row=1, anchor_col=1, shape=[[1]])

        # WHEN
        tetris_board.display_with_tetromino(mocked_screen, tetromino)

        # THEN
        self.assertEqual(mocked_screen.addstr.call_args_list[0][0], (0, 0, '* * * *'))
        self.assertEqual(mocked_screen.addstr.call_args_list[1][0], (1, 0, '* *   *'))
        self.assertEqual(mocked_screen.addstr.call_args_list[2][0], (2, 0, '*     *'))
        self.assertEqual(mocked_screen.addstr.call_args_list[3][0], (3, 0, '* * * *'))

    def test_is_tetromino_displayable_true_scenario(self):
        # GIVEN
        tetris_board = TetrisBoard(rows_num=4, cols_num=4)
        tetromino = Tetromino(drawing_area_size=1, anchor_row=1, anchor_col=1, shape=[[1]])

        # WHEN
        result = tetris_board.is_tetromino_displayable(tetromino)

        # THEN
        self.assertEqual(result, True)

    def test_is_tetromino_displayable_false_scenario(self):
        # GIVEN
        tetris_board = TetrisBoard(rows_num=4, cols_num=4)
        tetromino = Tetromino(drawing_area_size=1, anchor_row=0, anchor_col=0, shape=[[1]])

        # WHEN
        result = tetris_board.is_tetromino_displayable(tetromino)

        # THEN
        self.assertEqual(result, False)

    def test_no_valid_move_exists_for_tetromino_true_scenario(self):
        # GIVEN
        tetris_board = TetrisBoard(rows_num=4, cols_num=4)
        tetromino = Tetromino(drawing_area_size=1, anchor_row=2, anchor_col=2, shape=[[1]])

        # WHEN
        result = tetris_board.no_valid_move_exists_for_tetromino(tetromino)

        # THEN
        self.assertEqual(result, True)

    def test_no_valid_move_exists_for_tetromino_false_scenario(self):
        # GIVEN
        tetris_board = TetrisBoard(rows_num=4, cols_num=4)
        tetromino = Tetromino(drawing_area_size=1, anchor_row=1, anchor_col=1, shape=[[1]])

        # WHEN
        result = tetris_board.no_valid_move_exists_for_tetromino(tetromino)

        # THEN
        self.assertEqual(result, False)

    def test_save_new_state(self):
        # GIVEN
        tetris_board = TetrisBoard(rows_num=4, cols_num=4)
        tetromino = Tetromino(drawing_area_size=1, anchor_row=1, anchor_col=1, shape=[[1]])

        # WHEN
        tetris_board.save_new_state(tetromino)

        # THEN
        self.assertEqual(tetris_board.board, [
            ["*", "*", "*", "*"],
            ["*", "*", " ", "*"],
            ["*", " ", " ", "*"],
            ["*", "*", "*", "*"],
        ])
