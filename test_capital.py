# Unit Testing
# TDD 
# Write a failing test
# Make the test pass
# recurse to line 4 if line 3 doesn't apply for you

import pytest

def capital_case(string):
    if not isinstance(string, str):
        raise TypeError("The argument must be a string")
    return string.capitalize()

def test_capital_case():
    assert capital_case("david") == "David"

def test_raises_exception():
    with pytest.raises(TypeError):
        capital_case[1]