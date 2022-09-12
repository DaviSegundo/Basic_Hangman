"""
File that handles the implementation of game logic.
"""

import random
from dataclasses import dataclass, field

from src import utils
from src.display import Display


@dataclass
class Hangman:
    """
    Game class, where logic is implemented and defined.
    """

    display: Display

    lifes: int = field(init=False, default=6)
    word_list: list[str] = field(
        default_factory=lambda: ["davi", "segundo", "pinheiro"]
    )
    tried_letter_list: list[str] = field(init=False, default_factory=list)
    word: str = field(init=False)
    win: bool = field(init=False)
    output_format: str = field(init=False)

    def __post_init__(self):
        self.word = random.choice(self.word_list)
        self.output_format = utils.generate_output_format(self.word)
        self.win = False

    def show_general_info_display(self) -> None:
        """
        Function to center the default display view avoiding repetition of this
        entire block of code.
        """
        self.display.show_general_info(
            lifes=self.lifes,
            tried_letter_list=self.tried_letter_list,
            output_format=self.output_format,
        )

    def valid_input(self) -> str:
        """
        Validates user input, confirming it was a single letter.
        """
        valid = False
        char = ""
        while not valid:
            char = input("Chosse a letter: ")

            if 0 <= len(char) > 1 or not char.isalpha():
                self.show_general_info_display()
                print(f"Invalid letter attempted: {char}\n")
            elif char in self.tried_letter_list:
                self.show_general_info_display()
                print(f"Letter already attempted: {char}\n")
            else:
                valid = True

        return char

    def run(self) -> None:
        """
        Run the game and handles the execution flow.
        """
        while not self.win and self.lifes >= 1:
            if utils.check_win(self.output_format):
                self.display.show_win_info(word=self.word)
                self.win = True
                continue

            self.show_general_info_display()

            enter = self.valid_input()
            self.tried_letter_list.append(enter)

            if enter in self.word:
                idxs = utils.get_index_letter(word=self.word, letter=enter)
                self.output_format = utils.transform_output_format(
                    output_format=self.output_format, letter=enter, index_found=idxs
                )
            else:
                self.lifes -= 1

            if self.lifes == 0:
                self.display.show_lose_info(self.word)
