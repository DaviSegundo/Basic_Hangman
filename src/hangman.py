import random
from os import system
from dataclasses import dataclass, field

from src import utils
from src import display

clear = lambda: system("clear")


@dataclass
class Hangman:

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

    def valid_input(self) -> str:
        valid = False
        char = ""
        while not valid:
            char = input("Chosse a letter: ")

            if 0 <= len(char) > 1 or not char.isalpha():
                print("Invalid letter\n")
            elif char in self.tried_letter_list:
                print("Letter already tried\n")
            else:
                valid = True

        return char

    def run(self):
        while not self.win and self.lifes >= 1:
            clear()
            if utils.check_win(self.output_format):
                print("Word discovered correctly!")
                print(self.word)
                self.win = True
                continue

            display.get_general_info(
                self.lifes, self.tried_letter_list, self.output_format
            )
            enter = self.valid_input()
            self.tried_letter_list.append(enter)

            if enter in self.word:
                idxs = utils.get_index_letter(word=self.word, letter=enter)
                self.output_format = utils.transform_output_format(
                    output_format=self.output_format, letter=enter, index_found=idxs
                )
                print()
            else:
                print("Char not found in word")
                self.lifes -= 1
                print("\n")

            if self.lifes == 0:
                clear()
                print(display.get_display(self.lifes))
                print("You loose!")
