import pytest
from code_challenges.multi_bracket_validation.multi_bracket_validation import (
    multi_bracket_validation,
)


def test_true_round():
    input_str = "()()"
    actual = multi_bracket_validation(input_str)
    expected = True
    assert actual == expected