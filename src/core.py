# libs
import re
import math
import operator

class Engine:
    """
        Exeprimental class implementing own eval
    """
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        '!': math.factorial
    }

    const = {
        "pi": math.pi,
        "e": math.e
    }

    func = {
        "sin": math.sin,
        "cos": math.cos,
        "log": math.log,
    }

    def __call__(self, s: str):
    	return self._eval(s)

    def isnumber(self, n:str): # .isdigit() doesnt work for negative numbers
        try:
            float(n)
            return True
        except:
            return False

    def _handle_const(self, ret: list):
        for k, v in self.const.items():
            for idx, i in enumerate(ret):
                if k == i:
                    print(ret)
                    print(k, v, i, idx)
                    ret[idx] = float(v)
        return ret
        
    def _check_neg(self, ret: list):
        if len(ret) == 1: return ret # single number -> final result
        # find negative numbers
        for idx, i in enumerate(ret[:-1]):
            # example what is for loop doing: ["-", "1"] -> ["-1"]
            if i == "-" and self.isnumber(ret[idx+1]):
                ret[idx+1] = float(ret[idx+1]) * -1
                ret[idx] = "+"
                #print(ret)
                return self._check_neg(ret) # to not add complexity with offset, repeat recursion
        return ret # all negative numbers were handled
    
    def _compute_factorial(self, ret: list):
        if len(ret) == 1: return ret # single number -> final result
        for idx, i in enumerate(ret[1:]):
            if i == "!":
                n = int(ret[idx])
                assert n > 0 # n should be always positive number
                ret[idx:idx+2] = [float(self.ops["!"](n))]
                return self._compute_factorial(ret) # to not add complexity with offset, repeat recursion
        return ret
    
    def _compute(self, op: str, ret: list):
        assert op in self.ops.keys()
        if len(ret) == 1: return ret # single number -> final result
        for idx, i in enumerate(ret[1:-1]):
            if i == op: # op is ret[idx+1]
                if not self.isnumber(ret[idx]) or not self.isnumber(ret[idx+2]):
                    ret.pop(idx+1)
                    return self._compute(op, ret)
                n = self.ops[i](float(ret[idx]), float(ret[idx+2]))
                ret[idx:idx+3] = [float(n)]
                return self._compute(op, ret) # to not add complexity with offset, repeat recursion
        return ret
                    
    def _calculate(self, ret: list):
        ret = self._handle_const(ret)
        ret = self._check_neg(ret)
        ret = self._compute_factorial(ret)
        for op in "*/+":
            ret = self._compute(op, ret)
        if len(ret) == 3 and ret[0] == '(' and ret[2] == ')':
            return [str(ret[1])]
        return [str(ret[0])]

    def _check_func(self, ret: list):
        for k, v in self.func.items():
            for idx, i in enumerate(ret[:-1]):
                if i == k and self.isnumber(ret[idx+1]):
                        ret[idx:idx+2] = [str(v(float(ret[idx+1])))]
                        return self._check_func(ret)
        return ret
                
    def _eval(self, s: str):
        pattern = r"(\d+\.\d+|\d+|[()+\-*/!^]|pi|e|sin|cos|log)"
        ret = re.findall(pattern, s)
        return self._dive(ret)
        
    def _dive(self, ret: list):
        # get indexes of all '(' and ')'
        left_param = [i for i, string in enumerate(ret) if '(' in string]
        right_param = [i for i, string in enumerate(ret) if ')' in string]
        assert len(left_param) == len(right_param)
        
        if len(left_param) == 0: # no parenthesis
        	return self._calculate(ret) # end of recursion

 		# find deepest '()' and calculate it (rewrite it in ret)
        for i in right_param:
            for j in left_param[::-1]:
                # find deepest and closest '(' and ')'
                if i > j:
                    ret[j:i+1] = self._calculate(ret[j:i+1])
                    if len(ret) == 1: 
                        return float(ret)
                    ret = self._check_func(ret)
                    return self._eval(''.join(ret)) # to not add complexity with offset, repeat recursion


if __name__ == "__main__":
	c = Calc()
	test = "1+23-(3/(-2+3!))+pi+cos(1-(2-1)+sin(sin(1)))"
	print(f"{test=}")
	print(c._eval(test))
