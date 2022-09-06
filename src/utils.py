def get_index_letter(word: str, letter: str) -> list[int]:
    idx = [pos for pos, char in enumerate(word) if char == letter]

    return idx


def transform_output_format(
    output_format: str, letter: str, index_found: list[int]
) -> str:
    splited_list = output_format.split(" ")

    for idx in index_found:
        splited_list[idx] = letter

    return " ".join(splited_list)


def generate_output_format(word: str) -> str:
    return ("_ " * len(word))[:-1]


def check_win(output_format: str) -> bool:
    if "_" in output_format:
        return False
    return True
