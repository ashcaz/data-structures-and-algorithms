import pytest
from code_challenges.multi_bracket_validation.multi_bracket_validation import (
    multi_bracket_validation,
)


def test_empty_str():
    input_str = ""
    with pytest.raises(Exception) as e:
        multi_bracket_validation(input_str)

    assert str(e.value) == "Method can not be ran with an empty string"


def test_true_round():
    input_str = "()()"
    actual = multi_bracket_validation(input_str)
    expected = True
    assert actual == expected


def test_true_all():
    input_str = f"()[]{{}}"
    print(input_str)
    actual = multi_bracket_validation(input_str)
    expected = True
    assert actual == expected


def test_false_easy():
    input_str = "(]"
    actual = multi_bracket_validation(input_str)
    expected = False
    assert actual == expected


def test_false_hard():
    input_str = "([)]"
    actual = multi_bracket_validation(input_str)
    expected = False
    assert actual == expected


def test_lonely_bracket():
    input_str = "["
    actual = multi_bracket_validation(input_str)
    expected = False
    assert actual == expected