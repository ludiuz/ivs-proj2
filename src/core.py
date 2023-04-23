import re
import math
import operator


class Engine:
    """
    The core of the calculator. It uses recursive logic to dive into the deepest parentheses
    and computes recursively back. When there is a change in the size of the input list (ret),
    it goes back recursively to account for the new offset, eliminating the need to keep track
    of it (reducing code complexity). Each function is internal, and the only external function
    that should be used is __call__. The class does not handle 'wrong' inputs or incorrect syntax.
    It accepts a string resembling WolframAlpha syntax as input.
    """

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "^": operator.pow,
        "!": math.factorial,
    }

    const = {"pi": math.pi, "e": math.e}

    func = {
        "sin": math.sin,
        "cos": math.cos,
        "log": math.log,
    }

    def __call__(self, s: str):
        """The main entry point for the calculator."""
        return "".join(self._eval(s))

    def isnumber(self, n: str):
        """
        Check if the given string is a number. Unlike .isdigit(), this method
        works for negative numbers as well.
        """
        try:
            float(n)
            return True
        except:
            return False

    def _handle_const(self, ret: list):
        """
        Replace constants in the input list with their corresponding values.
        """
        for k, v in self.const.items():
            for idx, i in enumerate(ret):
                if k == i:
                    ret[idx] = float(v)
        return ret

    def _check_neg(self, ret: list):
        """
        Handle negative numbers in the input list. Convert them to positive numbers
        and replace their position with "+" or pop from the list.
        """
        if len(ret) == 1:
            return ret  # single number -> final result
        for idx, i in enumerate(ret[:-1]):
            if i == "-" and self.isnumber(ret[idx + 1]):
                ret[idx + 1] = float(ret[idx + 1]) * -1
                if idx != 0 and str(ret[idx - 1]) in "^*/+-":
                    ret.pop(idx)
                else:
                    ret[idx] = "+"
                return self._check_neg(ret)
        return ret  # all negative numbers were handled

    def _compute_factorial(self, ret: list):
        """
        Compute the factorial of a number in the input list.
        """
        if len(ret) == 1:
            return ret  # single number -> final result
        for idx, i in enumerate(ret[1:]):
            if i == "!":
                n = int(ret[idx])
                assert n > 0  # n should be always positive number
                ret[idx : idx + 2] = [float(self.ops["!"](n))]
                return self._compute_factorial(ret)
        return ret

    def _compute(self, op: str, ret: list):
        """
        Compute the result of the given operation in the input list.
        """
        assert op in self.ops.keys()
        if len(ret) == 1:
            return ret  # single number -> final result
        for idx, i in enumerate(ret[1:-1]):
            if i == op:
                if not self.isnumber(ret[idx]) or not self.isnumber(ret[idx + 2]):
                    ret.pop(idx + 1)
                    return self._compute(op, ret)
                n = self.ops[i](float(ret[idx]), float(ret[idx + 2]))
                ret[idx : idx + 3] = [float(n)]
                return self._compute(op, ret)
        return ret

    def _calculate(self, ret: list):
        """
        Perform calculations in the input list by following the order of operations.
        """
        ret = self._handle_const(ret)
        ret = self._check_neg(ret)
        ret = self._compute_factorial(ret)
        for op in "^*/+":
            ret = self._compute(op, ret)
        if len(ret) == 3 and ret[0] == "(" and ret[2] == ")":
            return [str(ret[1])]
        if len(ret) == 2 and ret[0] == "+":
            return [str(ret[1])]
        return [str(ret[0])]

    def _check_func(self, ret: list):
        """
        Evaluate functions in the input list.
        """
        for k, v in self.func.items():
            for idx, i in enumerate(ret[:-1]):
                if i == k and self.isnumber(ret[idx + 1]):
                    ret[idx : idx + 2] = [str(v(float(ret[idx + 1])))]
                    return self._check_func(ret)
        return ret

    def _eval(self, s: str):
        """
        Evaluate the given string using the regex pattern and return the result.
        """
        pattern = r"(\d+\.\d+|\d+|[()+\-*/!^]|pi|e|sin|cos|log)"
        ret = re.findall(pattern, s)
        return self._dive(ret)

    def _dive(self, ret: list):
        """
        Dive into the deepest parentheses in the input list and compute the result recursively.
        """
        left_param = [i for i, string in enumerate(ret) if "(" in string]
        right_param = [i for i, string in enumerate(ret) if ")" in string]
        assert len(left_param) == len(right_param)

        if len(left_param) == 0:  # no parenthesis
            return self._calculate(ret)  # end of recursion

        for i in right_param:
            for j in left_param[::-1]:
                if i > j:
                    ret[j : i + 1] = self._calculate(ret[j : i + 1])
                    if len(ret) == 1:
                        return float(ret)
                    ret = self._check_func(ret)
                    return self._eval("".join(ret))
