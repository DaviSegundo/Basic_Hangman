import random
from dataclasses import dataclass, field

from src import utils


@dataclass
class Hangman:

    lifes: int = 5
    word_list: list[str] = field(
        default_factory=lambda: ["davi", "segundo", "pinheiro"]
    )
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
                print("Invalid letter")
            else:
                valid = True

        return char

    def run(self):
        while not self.win and self.lifes >= 1:
            print(self.output_format)
            enter = self.valid_input()

            if enter in self.word:
                idxs = utils.get_index_letter(word=self.word, letter=enter)
                self.output_format = utils.transform_output_format(
                    output_format=self.output_format, letter=enter, index_found=idxs
                )
            else:
                print("Char not found in word")
                self.lifes -= 1
                print(f"{self.lifes} lifes remaing")
