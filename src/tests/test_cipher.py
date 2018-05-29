import pytest

from ..cipher import cypher_word, decipher_word


@pytest.mark.parametrize("test_input,expected", [
    ("holi", "104,111,108,105"),
    ("hola", "104,111,108,97"),
    ("lukeskywalker", "108,117,107,101,115,107,121,119,97,108,107,101,114"),
])
def test_cypher_word(test_input, expected):
    assert cypher_word(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("104,111,108,105", "holi"),
    ("104,111,108,97", "hola"),
    ("108,117,107,101,115,107,121,119,97,108,107,101,114", "lukeskywalker"),
])
def test_decipher_word(test_input, expected):
    assert decipher_word(test_input) == expected
