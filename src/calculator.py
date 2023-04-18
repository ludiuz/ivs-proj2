# scripts
import core
import syntax_filter as sf

class Calculator:
    def __init__(self):
        self.c = core.Engine()
        self.f = sf.SyntaxFilter()
        self.history = []

    def __call__(self, s: str):
        try:
	    # apply filter to user input for validating correctness
            s = self.f(s)
            # apply custom eval to compute input
            ret = float(self.c(s)[0])
            self.history.append(ret)
            return ret
        except SyntaxError as e:        return self._ret_error("SyntaxError", e)
        except ZeroDivisionError as e:  return self._ret_error("ZeroDivisionError", e)
        except ValueError as e:         return self._ret_error("ValueError", e)
        except OverflowError as e:      return self._ret_error("OverflowError", e)

    def _ret_error(self, error: str, error_msg: str):
        return (error, error_msg)
