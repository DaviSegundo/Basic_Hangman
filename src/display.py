def get_display(lifes: int) -> str:

    lifes_6 = r"""
   _________
  |        |
  |
  |
  |
__|__
    """

    lifes_5 = r"""
   _________
  |        |
  |        O
  |
  |
__|__
    """

    lifes_4 = r"""
   _________
  |        |
  |        O
  |        |
  |
__|__
    """

    lifes_3 = r"""
   _________
  |        |
  |        O
  |        |\
  |
__|__
    """

    lifes_2 = r"""
   _________
  |        |
  |        O
  |       /|\
  |
__|__
    """

    lifes_1 = r"""
   _________
  |        |
  |        O
  |       /|\
  |         \
__|__
    """

    lifes_0 = r"""
   _________
  |        |
  |        O
  |       /|\
  |       / \
__|__
    """

    display = {
        6: lifes_6,
        5: lifes_5,
        4: lifes_4,
        3: lifes_3,
        2: lifes_2,
        1: lifes_1,
        0: lifes_0,
    }

    return display.get(lifes, "")


def get_general_info(lifes: int, tried_letter_list: list, output_format: str):
    print(get_display(lifes))
    print(f"{lifes} lifes remaing\n")
    print(f"Tried letter: {tried_letter_list}")
    print(output_format)
