import pytest
from code_challenges.hashtable.hash_table import Hashtable

# @pytest.mark.skip("pending")
def test_create():
    hashtable = Hashtable()
    assert hashtable


# @pytest.mark.skip("pending")
def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash("spam")
    secondary = hashtable._hash("spam")
    assert initial == secondary


# @pytest.mark.skip("pending")
def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash("spam")

    assert actual >= 0
    assert actual < hashtable.size

    assert 0 <= actual < hashtable.size


# @pytest.mark.skip("pending")
def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash("listen")
    secondary = hashtable._hash("silent")
    assert initial == secondary


# @pytest.mark.skip("pending")
def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash("glisten")
    secondary = hashtable._hash("silent")
    assert initial != secondary