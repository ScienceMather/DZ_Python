from random import randint as rnd
from math import sqrt
Xrnd=int(rnd(1,1001))
Yrnd=int(rnd(1,1001))
Summ=Xrnd+Yrnd
Mult=Xrnd*Yrnd
print(Summ,Mult)
Disc= pow(Summ,2)+4*(-Mult)
Xnum=round((-Summ-sqrt(Disc))/2*-1)
Ynum=round((-Summ+sqrt(Disc))/2*-1)
print(Xnum,Ynum)