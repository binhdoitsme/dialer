from dialer.util.trie import Trie

import pytest


@pytest.fixture
def trie():
    t: Trie[float] = Trie()
    t.insert("4673", 0.9)
    t.insert("46732", 1.1)
    t.insert("467", 1.0)
    t.insert("468", 0.15)
    t.insert("46", 0.17)
    return t


def test_longest_match(trie: Trie[float]):
    assert trie.longest_match("4673212345") == ("46732", 1.1)
    assert trie.longest_match("4673412345") == ("4673", 0.9)
    assert trie.longest_match("4672212345") == ("467", 1.0)
    assert trie.longest_match("4683212345") == ("468", 0.15)
    assert trie.longest_match("4693212345") == ("46", 0.17)
    assert trie.longest_match("4473212345") == None


def test_insert(trie: Trie[float]):
    assert trie.longest_match("4673212345") == ("46732", 1.1)
    trie.insert("467321", 0.15)
    assert trie.longest_match("4673212345") == ("467321", 0.15)


if __name__ == "__main__":
    pytest.main()
