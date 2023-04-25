import re
import calculator as c

zoz = []
calc = c.Calculator()
with open("data.txt", "r") as f:
    for line in f.readlines():
        zoz = zoz + line.split()
print(zoz)
sum = ""
res_i = ""
for i in range(len(zoz)):
    sum = calc(str(sum) + "+" + zoz[i])
    res_i = calc(str(res_i) + "+" + zoz[i] + "^2")
    # print(res_i)
avg = calc(sum + "/" + str(len(zoz)))

# avg =
# average = sum(zoz)
