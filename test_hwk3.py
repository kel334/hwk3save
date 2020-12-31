from hwk3 import same_first_digit
from hwk3 import reverse
from hwk3 import is_palindrome
from hwk3 import str_to_ascii
from hwk3 import get_piece_value
from hwk3 import format_date


def test_same_first_digit_identical():
    assert same_first_digit(1, 1, 1)


def test_same_first_digit_differing_lengths():
    assert same_first_digit(1, 100, 100000)


def test_same_first_digit_simply_false():
    assert not same_first_digit(1, 2, 3)


def test_same_first_digit_almost_the_same():
    assert not same_first_digit(12, 22222, 3222222)


def test_reverse_empty_string():
    assert reverse("") == ""


def test_reverse_empty_single_char():
    assert reverse("I") == "I"


def test_reverse_alphabetic():
    assert reverse("abcdefg") == "gfedcba"


def test_reverse_symbolic():
    assert reverse("(1@3$)") == ")$3@1("


def test_is_palindrome_empty_string():
    assert is_palindrome("")


def test_is_palindrome_single_char():
    assert is_palindrome("M")


def test_is_palindrome_simple_odd_length():
    assert is_palindrome("racecar")


def test_is_palindrome_simple_even_length():
    assert is_palindrome("toot")


def test_is_palindrome_asymmetric_capitals():
    assert is_palindrome("RaceCar")


def test_is_palindrome_spaces():
    assert is_palindrome("lisa bonet ate no basil")


def test_is_palindrome_spaces_and_commas():
    assert is_palindrome("Lager, sir, is regal")


def test_is_palindrome_the_spaces_commas_and_apostrophes():
    assert is_palindrome("Go hang a salami, I\'m a lasagna hog")


def test_is_palindrome_simply_not():
    assert not is_palindrome("Hey, this isn\'t a palindrome!")


def test_str_to_ascii_empty_string():
    assert str_to_ascii("") == []


def test_str_to_ascii_alphabetic():
    assert str_to_ascii("abcdefg") == list(range(97, 104))


def test_str_to_ascii_capitals():
    assert str_to_ascii("ABCDEFG") == list(range(65, 72))


def test_str_to_ascii_symbolic():
    assert str_to_ascii("(1@3$)") == [40, 49, 64, 51, 36, 41]


def test_get_piece_value_pawn():
    assert get_piece_value("pawn") == 1


def test_get_piece_value_rook_with_capitals():
    assert get_piece_value("RoOk") == 5


def test_get_piece_value_forklift():
    assert get_piece_value("forklift") is None


def test_format_date_generic():
    assert format_date("17760704") == "July 4th, 1776"


def test_format_date_january():
    assert format_date("19250105") == "January 5th, 1925"


def test_format_date_december():
    assert format_date("19491227") == "December 27th, 1949"


def test_format_date_the_thirtyth():
    assert format_date("17760730") == "July 30th, 1776"


def test_format_date_the_first():
    assert format_date("17760701") == "July 1st, 1776"


def test_format_date_the_twelfth():
    assert format_date("17760712") == "July 12th, 1776"


def test_format_date_the_twentythird():
    assert format_date("17760723") == "July 23rd, 1776"


def test_format_date_the_thirtyth():
    assert format_date("17760730") == "July 30th, 1776"
