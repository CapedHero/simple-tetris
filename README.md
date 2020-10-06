# Simple-Tetris

+ This project implements a simplified version of a text-based game of Tetris.

+ Python 3.7 is required, as this project uses dataclasses. For Python 3.6
  there is a [backport](https://pypi.org/project/dataclasses/).

+ To play the game, call `python main.py` from the project's root directory.

+ There are no external dependencies i.e. the project uses only Python built-in
  libraries.

+ To run unit tests, call `python -m unittest discover src/tests -v`. Personally,
  I prefer to use pytest as a test runner. Yet for this project I have decided
  that it is more important to keep the code free from external dependencies.
