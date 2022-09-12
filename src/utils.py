"""
Functions responsible for dealing with some aspects of the game's operating logic.
"""


def get_index_letter(word: str, letter: str) -> list[int]:
    """
    Returns the indices found for the given letter within the word.
    """
    idx = [pos for pos, char in enumerate(word) if char == letter]

    return idx


def transform_output_format(
    output_format: str, letter: str, index_found: list[int]
) -> str:
    """
    Transforms the output word format, placing the informed letter in the indices that were passed
    and returning the terminal output format.
    """
    splited_list = output_format.split(" ")

    for idx in index_found:
        splited_list[idx] = letter

    return " ".join(splited_list)


def generate_output_format(word: str) -> str:
    """
    Generates the initial format of the word that needs to be guessed.
    """
    return ("_ " * len(word))[:-1]


def check_win(output_format: str) -> bool:
    """
    Checks if the player has won the game.
    """
    if "_" in output_format:
        return False
    return True
