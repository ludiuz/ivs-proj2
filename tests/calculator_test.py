import pytest

import calculator as c


def test_calculator():
    assert c.Calculator()("Bruh")[0] == "SyntaxError"
    assert c.Calculator()("pi/0")[0] == "ZeroDivisionError"
    assert c.Calculator()("4^(1/2)") == "2.0"


if __name__ == "__main__":
    test_calculator()
