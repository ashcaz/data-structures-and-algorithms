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


# @pytest.mark.skip("pending")
def test_set():
    hashtable = Hashtable()
    hashtable.set("number", 23)
    actual = hashtable.get("number")
    expected = 23
    assert actual == expected


# @pytest.mark.skip("pending")
def test_set_fail():
    hashtable = Hashtable()
    hashtable.set("number", 23)
    actual = hashtable.get("fail")
    expected = 23
    assert actual != expected


# @pytest.mark.skip("pending")
def test_get1(test_ht):
    actual = test_ht.get("number")
    expected = 23
    assert actual == expected


# @pytest.mark.skip("pending")
def test_get2(test_ht):
    actual = test_ht.get("letter")
    expected = "a"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_get_fail(test_ht):
    actual = test_ht.get("noun")
    expected = "a"
    assert actual != expected


# @pytest.mark.skip("pending")
def test_contains_true(test_ht):
    actual = test_ht.contains("number")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_contains_false(test_ht):
    actual = test_ht.contains("name")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_contains_fail(test_ht):
    actual = test_ht.contains("name")
    expected = True
    assert actual != expected


# *****************************************
# FIXTURES
# *****************************************


@pytest.fixture
def test_ht():
    hashtable = Hashtable()
    hashtable.set("number", 23)
    hashtable.set("letter", "a")
    hashtable.set("verb", "run")
    return hashtable
