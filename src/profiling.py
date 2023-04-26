import cProfile
import re
import calculator as c

zoz = []
calc = c.Calculator()
with open("data.txt", "r") as f:
    zoz = zoz + f.read().split()
    # for line in f.readlines():
    # zoz = zoz + line.split()
# print(zoz)
print("somtu")


def calculate():
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
        # print(i)

    avg = calc(sum + "/" + str(len(zoz)))
    first = calc((str(res_i) + "-" + str(len(zoz)) + "*(" + avg + ")^2"))
    res_2 = calc("(1/(" + str(len(zoz)) + "-1))*" + first)
    res = calc("(" + str(res_2) + ")^(1/2)")
    return res


# print(calculate())

cProfile.run("calculate()")
