import pytest

import syntax_filter as sf


def test_syntax_filter():
    def test(s: str):
        with pytest.raises(SyntaxError):
            sf.SyntaxFilter()(s)

    test("I'm never gonna give you up")
    test("3+2(")
    test("ee")
    test(")5*1(")
    test("(4-2)(1/2)")
    test("(3-1)pi")
    test("--1")
    test("2+")
    test("!3")

    sf.SyntaxFilter()("(((e)-(pi))+1)")
    sf.SyntaxFilter()("(1!)^2%3*4/5+6-7")


if __name__ == "__main__":
    test_syntax_filter()
