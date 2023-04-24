import math
import re


class SyntaxFilter:
    """
    Parses the input to ensure it resembles WolframAlpha-like syntax.
    Designed to be used before the Engine() class.
    The only external function that should be used is __call__.
    The class doesn't return anything; it only raises SyntaxError if the input is invalid.
    """

    valid_chars = set("0123456789+-^*/().!")
    special_op = [("sin", "S"), ("log", "L"), ("tan", "T")]
    special_n = [("pi", "P"), ("e", "E")]

    def __call__(self, s: str):
        """
        Check if the input string has valid syntax and operations.
        """
        return self._check_operations(s)

    def _check_operations(self, s: str):
        """
        Check for any invalid syntax or invalid operation combinations in the input string.
        """

        # string of operations
        _op = "^*/+-"

        # check number of parenthesis and their order (get indexes)
        left_param = [i for i, string in enumerate(s) if "(" in string]
        right_param = [i for i, string in enumerate(s) if ")" in string]
        if len(left_param) != len(right_param):
            raise SyntaxError
        # check correct order of parenthesis 
        n = 0
        for i, j in zip(left_param, right_param):
            if j < i: n += -1
            elif i > j: n += 1
            if n < 0: raise SyntaxError

        # Replace special operations and special numbers with their corresponding characters
        for str_, char in self.special_op + self.special_n:
            if str_ in s:
                pattern = r"(?<![0-9A-Za-z])" + re.escape(str_) + r"(?![0-9A-Za-z])"
                s = re.sub(pattern, char, s)

        #pattern = r"(\d+\.\d+|\d+|[()+\-*/!^]|P|E|S|C|L|T)"
        #ds = re.findall(pattern, s)
        #print(ds)

        # Check if any special numbers + numbers are followed by an opening parenthesis
        for _, char in self.special_n + [(None, str(i)) for i in range(0, 10)]:
            if f"{char}(" in s:
                raise SyntaxError
            if f"){char}" in s:
                raise SyntaxError

        # Check if two parentheses are adjacent
        if ")(" in s:
            raise SyntaxError
        
        # check if operations are next to each others + check if factorial is attached to operation
        if len(s) > 1:
            for idx in range(len(s[:-1])):
                if s[idx] in _op and s[idx+1] in _op:
                    raise SyntaxError
                if (s[idx] in _op+"(") and (s[idx+1] == "!"):
                    raise SyntaxError

        # check edges
        if s[-1] in _op+"(":
            raise SyntaxError
        if s[0] in "!^*/":
            raise SyntaxError

        # include all special characters assigned to special operations and special numbers
        extended_valid_chars = self.valid_chars.copy()
        for _, char in self.special_op + self.special_n:
            extended_valid_chars.add(char)
        # Check if only valid characters are in the string
        if all(c in extended_valid_chars for c in s) != True:
            raise SyntaxError

#if __name__ == "__main__":
#    sf = SyntaxFilter()
#    sf("*3+2*")