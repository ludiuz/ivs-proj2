import re
import math
import operator

class Calc:
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        '!': math.factorial
    }
    def _check_num(self, ret: list):
        if len(ret) == 1: return float(ret) # single number -> final result
        # because of negative number logic, if two numbers are next to each other
        idx = 0
        for i, j in zip(ret, ret[1:]):
            if i.isdigit() and j.isdigit():
                ret[idx:idx+2] = float(i)+float(j)
                return self._check_num(ret) # to not add complexity with offset, repeat recursion
            idx += 1
        return ret
        
    def _check_neg(self, ret: list):
        if len(ret) == 1: return float(ret) # single number -> final result
        # find negative numbers
        for idx, i in enumerate(ret[:-1]):
            # example what is for loop doing: ["-", "1"] -> ["-1"]
            if i == "-" and ret[idx+1].isdigit():
                ret[idx:idx+2] = float(ret[idx+1]) * -1
                return self._check_neg(ret) # to not add complexity with offset, repeat recursion
        return ret # all negative numbers were handled
    
    def _compute_factorial(self, ret: list):
        if len(ret) == 1: return float(ret) # single number -> final result
        for idx, i in enumerate(ret[1:]):
            if i == "!":
                ret[idx:idx+2] = self.ops["!"](float(ret[idx]))
                self._compute_factorial(ret) # to not add complexity with offset, repeat recursion
        return ret
    
    def _compute(self, op: str, ret: list):
        assert op in self.ops.keys()
        if len(ret) == 1: return float(ret) # single number -> final result
        for idx, i in enumerate(ret[1:]):
            if i == op: # op is ret[idx+1]
                ret[idx:idx+3] = self.ops[i](float(ret[idx]), float(ret[idx+2]))
                self._compute(ret) # to not add complexity with offset, repeat recursion
        return ret
                    
    def _calculate(self, s: list):
        ret = self._check_neg(s)
        ret = self._compute_factorial(ret)
        for op in "*/+-":
            ret = self._compute(op, ret)
        ret = self._check_num(ret)
        return float(ret)       
                
    def _eval(self, s: str):
        pattern = r"(\d+|[()+\-*\/!^])"
        ret = re.findall(pattern, s)
        return self._dive(ret)
        
    def _dive(self, s: list):
        # get indexes of all '(' and ')'
        left_param = [i for i, string in enumerate(s) if '(' in string]
        right_param = [i for i, string in enumerate(s) if ')' in string]
        assert len(left_param) == len(right_param)
        
        if len(left_param) == 0: # no parenthesis
        	return _calculate(ret) # end of recursion

 		# find deepest '()' and calculate it (rewrite it in ret)
        for i in right_param:
            for j in left_param.reverse():
                # find deepest and closest '(' and ')'
                if i > j:
                    s[j:i+1] = self._calculate(s[j:i+1])
                    if len(ret) == 1: 
                        return float(ret)
                    return _eval(''.join(s)) # to not add complexity with offset, repeat recursion


c = Calc()
print(c._eval("1+23-(3/(-2))!"))
