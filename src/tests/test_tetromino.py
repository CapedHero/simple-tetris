import unittest
from unittest import mock

from src.tetromino import Tetromino


class TestTetromino(unittest.TestCase):
    # fmt: off
    TETROMINO_SHAPE = [
        [1, 0],
        [0, 0],
    ]
    # fmt: on

    @mock.patch(
        "src.tetromino.TETROMINO_SHAPES",
        {"THIS_SHOULD_NOT_BE_RETURNED": [], "MOCKED_TETROMINO_SHAPE": TETROMINO_SHAPE},
    )
    @mock.patch("src.tetromino.random")
    def test_create_random_tetromino(self, mocked_random):
        # GIVEN
        mocked_random.choice.side_effect = lambda x: x[1]
        mocked_random.randint.return_value = 123
        tetris_board_cols_num = 10

        # WHEN
        tetromino = Tetromino.create_random_tetromino(tetris_board_cols_num)

        # THEN
        self.assertEqual(tetromino.drawing_area_size, len(self.TETROMINO_SHAPE))
        self.assertEqual(tetromino.anchor_row, 1)
        self.assertEqual(tetromino.anchor_col, 123)
        self.assertEqual(tetromino.shape, self.TETROMINO_SHAPE)

    def test_move_left(self):
        # GIVEN
        anchor_row = 3
        anchor_col = 4
        tetromino = Tetromino(
            drawing_area_size=2,
            anchor_row=anchor_row,
            anchor_col=anchor_col,
            shape=self.TETROMINO_SHAPE,
        )

        # WHEN
        tetromino.move_left()

        # THEN
        self.assertEqual(tetromino.anchor_row, anchor_row + 1)
        self.assertEqual(tetromino.anchor_col, anchor_col - 1)

    def test_move_right(self):
        # GIVEN
        anchor_row = 3
        anchor_col = 4
        tetromino = Tetromino(
            drawing_area_size=2,
            anchor_row=anchor_row,
            anchor_col=anchor_col,
            shape=self.TETROMINO_SHAPE,
        )

        # WHEN
        tetromino.move_left()

        # THEN
        self.assertEqual(tetromino.anchor_row, anchor_row + 1)
        self.assertEqual(tetromino.anchor_col, anchor_col - 1)

    def test_rotate_clockwise(self):
        # GIVEN
        anchor_row = 3
        anchor_col = 4
        tetromino = Tetromino(
            drawing_area_size=2,
            anchor_row=anchor_row,
            anchor_col=anchor_col,
            shape=self.TETROMINO_SHAPE,
        )

        # WHEN
        tetromino.rotate_clockwise()

        # THEN
        self.assertEqual(tetromino.anchor_row, anchor_row + 1)
        # fmt: off
        self.assertEqual(tetromino.shape, [
            [0, 1],
            [0, 0],
        ])
        # fmt: on

    def test_rotate_counterclockwise(self):
        # GIVEN
        anchor_row = 3
        anchor_col = 4
        tetromino = Tetromino(
            drawing_area_size=2,
            anchor_row=anchor_row,
            anchor_col=anchor_col,
            shape=self.TETROMINO_SHAPE,
        )

        # WHEN
        tetromino.rotate_counterclockwise()

        # THEN
        self.assertEqual(tetromino.anchor_row, anchor_row + 1)
        # fmt: off
        self.assertEqual(tetromino.shape, [
            [0, 0],
            [1, 0],
        ])
        # fmt: on
