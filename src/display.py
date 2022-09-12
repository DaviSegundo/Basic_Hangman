"""
This module handles the class responsible for displaying information on the screen.
"""

from os import system
from dataclasses import dataclass


@dataclass
class Display:
    """
    Class that deals with the information that will be shown on the screen, separated into functions
    that match the message format.
    """

    picture_dict: dict[int, str]

    def clear(self) -> None:
        """
        Clear the terminal to remove previous information.
        """
        system("clear")

    def get_picture(self, lifes: int) -> str:
        """
        Retrieves the image that should be shown based on remaining lives.
        """
        return self.picture_dict.get(lifes, "")

    def show_general_info(
        self, lifes: int, tried_letter_list: list, output_format: str
    ) -> None:
        """
        Shows general game information.
        """
        self.clear()
        print("Hangman Game")
        print(self.get_picture(lifes))
        print(f"{lifes} lifes remaing\n")
        print(f"Attempted letters: {tried_letter_list}\n")
        print(output_format)
        print()

    def show_win_info(self, word: str) -> None:
        """
        Shows the information when the player wins the game.
        """
        self.clear()
        print("Word guessed correctly!")
        print(f"The word was: {word}")

    def show_lose_info(self, word: str) -> None:
        """
        Shows the information when the player loses the game.
        """
        self.clear()
        print(self.get_picture(0))
        print("You lose!")
        print(f"The word was: {word}")
