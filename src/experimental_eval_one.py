import math

class Calculator:
    def _eval(self, s: str) -> float:
        def parse_expression(expr: str) -> float:
            if "(" in expr:
                open_paren = -1
                close_paren = -1
                for i, c in enumerate(expr):
                    if c == "(":
                        open_paren = i
                    elif c == ")":
                        close_paren = i
                        break

                left = expr[:open_paren]
                inner = expr[open_paren + 1:close_paren]
                right = expr[close_paren + 1:]
                return parse_expression(left + str(parse_expression(inner)) + right)
            else:
                return parse_term(expr)

        def parse_term(term: str) -> float:
            if "+" in term:
                return sum(map(parse_term, term.split("+")))
            else:
                return parse_signed_factor(term)

        def parse_signed_factor(factor: str) -> float:
            if factor.startswith("-"):
                return -parse_factor(factor[1:])
            else:
                return parse_factor(factor)

        def parse_factor(factor: str) -> float:
            if "-" in factor:
                parts = factor.split("-")
                result = parse_element(parts[0])
                for part in parts[1:]:
                    result -= parse_element(part)
                return result
            else:
                return parse_element(factor)

        def parse_element(element: str) -> float:
            if "*" in element or "/" in element:
                result = 1
                for e in element.split("*"):
                    if "/" in e:
                        numerator, denominator = e.split("/")
                        numerator, denominator = numerator.strip(), denominator.strip()
                        if numerator:
                            result *= parse_base(numerator)
                        if denominator:
                            result /= parse_base(denominator)
                    else:
                        e = e.strip()
                        if e:
                            result *= parse_base(e)
                return result
            else:
                return parse_base(element)

        def parse_base(base: str) -> float:
            if "^" in base:
                base, exponent = base.split("^")
                return float(base) ** float(exponent)
            elif "!" in base:
                return math.factorial(int(base[:-1]))
            else:
                return float(base)

        return parse_expression(s)


calc = Calculator()
print(calc._eval("31-1"))  # 30
print(calc._eval("3*(2-1)"))  # 3
print(calc._eval("2/4^(1/2)"))  # 1
print(calc._eval("(3!)-1*(2+1)+(1*(-1*(1-2)))"))  # 4
print(calc._eval("(3*(-3)+3!-1)+1"))  # -3
print(calc._eval("-1+(3*2)+(1+(-2-1))"))  # 3
