"""
Handles general testing of game features.
"""

from src import utils


class TestGetIndexLetter:
    """
    Class to test the functionality of getting the letter index in the word.
    """

    def test_get_index_letter_1(self):
        word = "davi"
        letter = "a"

        index = utils.get_index_letter(word=word, letter=letter)

        assert index == [1]

    def test_get_index_letter_2(self):
        word = "pinheiro"
        letter = "i"

        index = utils.get_index_letter(word=word, letter=letter)

        assert index == [1, 5]

    def test_get_index_letter_3(self):
        word = "aaa"
        letter = "a"

        index = utils.get_index_letter(word=word, letter=letter)

        assert index == [0, 1, 2]

    def test_get_index_letter_empty(self):
        word = "davi"
        letter = "w"

        index = utils.get_index_letter(word=word, letter=letter)

        assert index == []


class TestTransformOutput:
    """
    Class to test the functionality transform the word in the output.
    """

    def test_transform_output_format_basic(self):
        out = "_ _ _ _"
        letter = "a"
        idxs = [1]

        output_format = utils.transform_output_format(
            output_format=out, letter=letter, index_found=idxs
        )

        assert output_format == "_ a _ _"

    def test_transform_output_format_1(self):
        out = "_ _ _ _ _ _ _ _"
        letter = "i"
        idxs = [1, 5]

        output_format = utils.transform_output_format(
            output_format=out, letter=letter, index_found=idxs
        )

        assert output_format == "_ i _ _ _ i _ _"

    def test_transform_output_format_2(self):
        out = "_ i _ _ _ i _ _"
        letter = "p"
        idxs = [0]

        output_format = utils.transform_output_format(
            output_format=out, letter=letter, index_found=idxs
        )

        assert output_format == "p i _ _ _ i _ _"

    def test_transform_output_format_3(self):
        out = "p i _ _ _ i _ _"
        letter = "w"
        idxs = []

        output_format = utils.transform_output_format(
            output_format=out, letter=letter, index_found=idxs
        )

        assert output_format == "p i _ _ _ i _ _"


class TestGenerateOutputFormat:
    """
    Class to test the functionality to generate the initial output format.
    """

    def test_generate_output_format_1(self):
        word = "davi"

        output_format = utils.generate_output_format(word=word)

        assert output_format == "_ _ _ _"

    def test_generate_output_format_2(self):
        word = "aa"

        output_format = utils.generate_output_format(word=word)

        assert output_format == "_ _"


class TestCheckWin:
    """
    Class to test the functionality of the player having won.
    """

    def test_check_win_true(self):
        output_format = "d a v i"

        win = utils.check_win(output_format=output_format)

        assert win == True

    def test_check_win_false(self):
        output_format = "d a v _"

        win = utils.check_win(output_format=output_format)

        assert win == False
