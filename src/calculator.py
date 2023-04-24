import core
import syntax_filter as sf


class Calculator:
    """
    A calculator class that takes a string representing a mathematical expression as input and returns
    the result of the expression or an error. It applies a syntax filter to validate the input and then
    computes the result using the core engine. It also maintains a history of the results.

    The calculator may return the following errors:
    - SyntaxError: If the input doesn't pass the requirements of the SyntaxFilter class.
    - ZeroDivisionError: If a division by zero occurs during computation in the Engine class.
    - ValueError: If an invalid value is encountered during computation in the Engine class.
    - OverflowError: If an overflow occurs during computation in the Engine class.
    """

    def __init__(self):
        """
        Initialize the calculator with the core engine, syntax filter, and an empty history.
        """
        self.c = core.Engine()
        self.f = sf.SyntaxFilter()
        self.history = []

    def __call__(self, s: str):
        """
        Validate and compute the input string, then return the result.
        If an error occurs, return the error type and message.
        """
        if s == "": return s # empty input
        try:
            # Apply filter to user input to validate its correctness
            self.f(s)
            # Apply custom eval to compute input
            ret = self.c(str(s))
            self.history.append(ret)
            return ret
        except SyntaxError as e: # occur in SyntaxFilter
            return self._ret_error("SyntaxError", e)
        except ZeroDivisionError as e: # occur in Engine
            return self._ret_error("ZeroDivisionError", e)
        except ValueError as e: # occur in Engine using factorial
            return self._ret_error("ValueError", e)
        except OverflowError as e: # can occur anywhere (most probably in Engine)
            return self._ret_error("OverflowError", e)

    def _ret_error(self, error: str, error_msg: str):
        """
        Return a tuple containing the error type and message.
        """
        return (error, error_msg)

#if __name__ == "__main__":
#    c = Calculator()
#    print(1, c("-1"))
#    print(2, c("5/0"))