import random
from dataclasses import dataclass
from typing import List


# fmt: off
TETROMINO_SHAPES = {
    "LR_TETROMINO_SHAPE":  [
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
    ],
    "LL_TETROMINO_SHAPE": [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 0],
    ],
    "STRAIGHT_TETROMINO_SHAPE": [
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ],
    "SKEW_TETROMINO_SHAPE": [
        [0, 1, 0],
        [1, 1, 0],
        [1, 0, 0],
    ],
    "SQUARE_TETROMINO_SHAPE": [
        [1, 1],
        [1, 1],
    ],
}
# fmt: on


@dataclass
class Tetromino:
    """
    Class for geometric shape used in Tetris.

    A tetromino is a geometric shape composed of four squares, connected
    orthogonally (i.e. at the edges and not the corners). See more at:
    https://en.wikipedia.org/wiki/Tetromino
    """

    drawing_area_size: int
    anchor_row: int
    anchor_col: int
    shape: List[List[int]]

    @classmethod
    def create_random_tetromino(cls, tetris_board_cols_num: int) -> "Tetromino":
        random_tetromino_shape = random.choice(list(TETROMINO_SHAPES.values()))
        random_tetromino = cls(
            drawing_area_size=len(random_tetromino_shape),
            anchor_row=1,
            anchor_col=random.randint(1, tetris_board_cols_num - len(random_tetromino_shape)),
            shape=random_tetromino_shape,
        )
        return random_tetromino

    def move_left(self) -> None:
        self.anchor_row += 1
        self.anchor_col -= 1

    def move_right(self) -> None:
        self.anchor_row += 1
        self.anchor_col += 1

    def rotate_clockwise(self) -> None:
        self.anchor_row += 1
        self.shape = list(map(list, zip(*self.shape[::-1])))

    def rotate_counterclockwise(self) -> None:
        self.anchor_row += 1
        self.shape = list(map(list, zip(*self.shape)))[::-1]
