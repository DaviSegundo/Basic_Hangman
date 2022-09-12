from os import system
from dataclasses import dataclass


@dataclass
class Display:

    picture_dict: dict[int, str]

    def clear(self) -> None:
        system("clear")

        return None

    def get_picture(self, lifes: int) -> str:
        return self.picture_dict.get(lifes, "")

    def show_general_info(
        self, lifes: int, tried_letter_list: list, output_format: str
    ) -> None:
        self.clear()
        print("Hangman Game")
        print(self.get_picture(lifes))
        print(f"{lifes} lifes remaing\n")
        print(f"Attempted letters: {tried_letter_list}\n")
        print(output_format)
        print()

        return None

    def show_win_info(self, word: str) -> None:
        self.clear()
        print("Word guessed correctly!")
        print(f"The word was: {word}")

        return None

    def show_lose_info(self, word: str) -> None:
        self.clear()
        print(self.get_picture(0))
        print("You lose!")
        print(f"The word was: {word}")

        return None
