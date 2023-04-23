import math
import re


class SyntaxFilter:
    """
    Parses the input to ensure it resembles WolframAlpha-like syntax.
    Designed to be used before the Engine() class.
    The only external function that should be used is __call__.
    The class doesn't return anything; it only raises SyntaxError if the input is invalid.
    """

    valid_chars = set("0123456789+-^*/().")
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
        # include all special characters assigned to special operations and special numbers
        extended_valid_chars = self.valid_chars.copy()
        for _, char in self.special_op + self.special_n:
            extended_valid_chars.add(char)

        # Replace special operations and special numbers with their corresponding characters
        for str_, char in self.special_op + self.special_n:
            if str_ in s:
                pattern = r"(?<![0-9A-Za-z])" + re.escape(str_) + r"(?![0-9A-Za-z])"
                s = re.sub(pattern, char, s)

        # Check if any special numbers are followed by an opening parenthesis
        for _, char in self.special_n + [(None, str(i)) for i in range(0, 10)]:
            if f"{char}(" in s:
                raise SyntaxError
            if f"){char}" in s:
                raise SyntaxError

        # Check if two parentheses are adjacent
        if ")(" in s:
            raise SyntaxError

        # Check if only valid characters are in the string
        if all(c in extended_valid_chars for c in s) != True:
            raise SyntaxError
