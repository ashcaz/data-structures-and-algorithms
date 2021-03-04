import pytest

from code_challenges.insertion_sort.insertion_sort import sort_func


def test_sort_empty_list():
    empty_list = []
    actual = sort_func(empty_list)
    expected = []
    assert actual == expected


def test_sort_output1():
    sort_list = [8, 4, 23, 42, 16, 15]
    actual = sort_func(sort_list)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_not_sort_output1():
    sort_list = [8, 4, 23, 42, 16, 15]
    actual = sort_func(sort_list)
    expected = [4, 8, 23, 15, 16, 42]
    assert actual != expected


def test_sort_output2():
    sort_list = [20, 18, 12, 8, 5, -2]
    actual = sort_func(sort_list)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_not_sort_output2():
    sort_list = [20, 18, 12, 8, 5, -2]
    actual = sort_func(sort_list)
    expected = [-2, 5, 8, 12]
    assert actual != expected


def test_sort_output3():
    sort_list = [5, 12, 7, 5, 5, 7]
    actual = sort_func(sort_list)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_not_sort_output3():
    sort_list = [5, 12, 7, 5, 5, 7]
    actual = sort_func(sort_list)
    expected = [5, 5, 7, 5, 7, 12]
    assert actual != expected


def test_sort_output4():
    sort_list = [2, 3, 5, 7, 13, 11]
    actual = sort_func(sort_list)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_not_sort_output4():
    sort_list = [2, 3, 5, 7, 13, 11]
    actual = sort_func(sort_list)
    expected = [3, 2, 5, 7, 11, 13]
    assert actual != expected