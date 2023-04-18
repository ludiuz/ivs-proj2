# libs
import math
import re

class SyntaxFilter:
    """
    Add later description
    """
    valid_chars = set("0123456789+-^*/().")
    special_op = [("sin", "S"), ("log", "L"), ("tan", "T")]
    special_n = [("pi", "P"), ("e", "E")]
        
    def __call__(self, s: str):
        self._check_operations(s)
        return self._rewrite_chars(s)

    def _check_operations(self, s: str):
        # include all special characters assigned to special operations and special numbers
        extended_valid_chars = self.valid_chars.copy()
        for _, char in (self.special_op + self.special_n):
            extended_valid_chars.add(char)

        for str_, char in self.special_op + self.special_n:
            if str_ in s:
                pattern = r'(?<![0-9A-Za-z])' + re.escape(str_) + r'(?![0-9A-Za-z])'
                s = re.sub(pattern, char, s)

        # Check if any special numbers are followed by an opening parenthesis
        for _, char in self.special_n+[(None, str(i)) for i in range(0, 10)]:
            if f"{char}(" in s:
                raise SyntaxError
            if f"){char}" in s:
                raise SyntaxError
        # check if two parenthesis are next to themself
        if ")(" in s: raise SyntaxError

        # check if only valid characters are in string
        if all(c in extended_valid_chars for c in s) != True:
            raise SyntaxError

    def _rewrite_chars(self, s: str):
        ret = s.replace('^', '**')
        return ret
