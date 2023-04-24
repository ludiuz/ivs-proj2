import pytest

import core


def test_engine():
    # test constants
    assert core.Engine()("7") == "7", f"Expected output '7' for input '7'"

    assert (
        core.Engine()("e") == f"2.718281828459045"
    ), f"Expected output '2.718281828459045' for input 'e'"

    assert (
        core.Engine()("pi") == "3.141592653589793"
    ), f"Expected output '3.141592653589793' for input 'pi'"

    assert (
        core.Engine()("2^(1/2)") == "1.4142135623730951"
    ), f"Expected output '1.4142135623730951' for input '2^(1/2)'"

    # test operations
    assert core.Engine()("7+7+0") == "14.0", "Expected output '14' for input '7+7+0'"

    assert (
        core.Engine()("3-5-0-1") == "-3.0"
    ), "Expected output '-2.' for input '3-5-0-1'"

    assert core.Engine()("2*3") == "6.0", "Expected output '6' for input '2*3'"

    assert core.Engine()("0*3.14") == "0.0", "Expected output '0.0' for input '0*3.14'"

    assert (
        core.Engine()("4/3") == "1.3333333333333333"
    ), "Expected output '1.3333333333333333' for input '4/3'"

    assert (
        core.Engine()("0/8.9167") == "0.0"
    ), "Expected output '0.0' for input '0/8.9167'"

    assert (
        core.Engine()("pi/e") == "1.1557273497909217"
    ), "Expected output '1.1557273497909217' for input 'pi/e'"

    with pytest.raises(ZeroDivisionError):
        core.Engine()("1/0")

    assert (
        core.Engine()("10!") == "3628800.0"
    ), "Expected output '3628800' for input '10!'"

    assert (
        core.Engine()("2^(-4)") == "0.0625"
    ), "Expected output '0.0625' for input '2^(-4)'"

    # test math functions

    assert (
        core.Engine()("sin(6)") == "-0.27941549819892586"
    ), "Expected output '-0.27941549819892586' for input 'sin(6)'"

    assert (
        core.Engine()("cos(-5)") == "0.28366218546322625"
    ), "Expected output '0.28366218546322625' for input 'cos(-5)'"

    assert core.Engine()("log(e)") == "1.0", "Expected output '1.0' for input 'log(e)'"

    assert (
        core.Engine()("log(2)/log(3)") == "0.6309297535714574"
    ), "Expected output '0.6309297535714574' for input 'log(2)/log(3)'"

    # test example inputs
    assert (
        core.Engine()("1+23-(3/(-2+3!))+pi+cos(1-(2-1)+sin(sin(1)))")
        == "27.12625726236585"
    ), "Expected output '27.12625726236585' for input '1+23-(3/(-2+3!))+pi+cos(1-(2-1)+sin(sin(1)))'"


if __name__ == "__main__":
    test_engine()
