import cProfile
import re
import calculator as c

zoz = []
calc = c.Calculator()

# Open file and read data into list
with open("data.txt", "r") as f:
    zoz = zoz + f.read().split()

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
        if i == 100000:
            print("ano")
        if i == 200000:
            print("ano")
        if i == 500000:
            print("ano")
        sum = calc(sum + "+" + zoz[i])
        res_i = calc(res_i + "+" + zoz[i] + "^2")

    # Calculate the average
    avg = calc(sum + "/" + str(len(zoz)))

    # Calculate the variance
    first = calc((str(res_i) + "-" + str(len(zoz)) + "*(" + avg + ")^2"))
    res_2 = calc("(1/(" + str(len(zoz)) + "-1))*" + first)

    # Calculate the standard deviation
    res = calc("(" + str(res_2) + ")^(1/2)")
    return res

# Run the calculate function using cProfile
cProfile.run("calculate()")
