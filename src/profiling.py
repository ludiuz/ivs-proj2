import cProfile
import sys
import calculator as c

zoz = []
calc = c.Calculator()
# Read data from stdin into list
zoz = sys.stdin.read().strip().split()

def calculate():
    """
    This function calculates deviation of the list of numbers
    contained in 'data.txt'.

    :returns: The deviation of the list of numbers.
    :rtype: float
    """
    sum = ""
    res_i = ""
    for i in range(len(zoz)):
        sum = calc(sum + "+" + zoz[i], True)
        res_i = calc(res_i + "+" + zoz[i] + "^2", True)

    # Calculate the average
    avg = calc(sum + "/" + str(len(zoz)), True)

    # Calculate the variance
    first = calc((str(res_i) + "-" + str(len(zoz)) + "*(" + avg + ")^2"), True)
    res_2 = calc("(1/(" + str(len(zoz)) + "-1))*" + first, True)

    # Calculate the standard deviation
    res = calc("(" + str(res_2) + ")^(1/2)" , True)
    return res

#print(calculate())
# Run the calculate function using cProfile
cProfile.run("calculate()")
