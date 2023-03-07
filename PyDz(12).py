from random import randint as rnd
chislo = int(input('Vvedite kol-vo kystov : '))
kysti = []
for i in range(chislo):
    kysti.append(rnd(1, 3))
count = 0
for i in range(chislo):
    if kysti[0] + kysti[-1] + kysti[1] > count:
        count = kysti[0] + kysti[-1] + kysti[1]
    kysti.insert(0, kysti[-1])
    kysti.pop()
print(kysti,'\n',count)
print()