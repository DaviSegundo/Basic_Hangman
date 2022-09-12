"""
Main file.
Where game dependencies are launched.
"""

from src.hangman import Hangman
from src.display import Display
from src.pictures import pictures

if __name__ == "__main__":
    display = Display(picture_dict=pictures)
    game = Hangman(display=display)
    game.run()
