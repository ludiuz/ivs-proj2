import re
import calculator as c

zoz = []
calc = c.Calculator()
with open('data.txt' , 'r') as f:
    #zoz = zoz + f.read().split()
    for line in f.readlines():
        zoz = zoz + line.split()
print(zoz)
sum = ""
res_i = ""
for i in range(len(zoz)):
    sum = calc(str(sum) + '+' + zoz[i])
    res_i = calc(str(res_i) + '+' + zoz[i] + '^2')
    #print(res_i)
avg = calc(sum + '/' + str(len(zoz)))
first = calc((str(res_i) +'-'+ str(len(zoz))+'*('+ avg + ')^2'))
print(first)
res_2 = calc('(1/(' + str(len(zoz)) + '-1))*' + first)
res = calc('('+ str(res_2) + ')^(1/2)')
print(res)
#avg = 
#average = sum(zoz)