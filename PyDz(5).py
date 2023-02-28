from random import randint as rnd,choice as rnc
otvet=None
print('Vvedite kolichestvo monet : ')
coins=int(input())
spisok=[]
for i in range(coins):
    spisok.append(rnd(0,1))
list_z=[]
list_o=[]
for i in spisok:
    if i == 0:
        list_z.append(i)
    elif i == 1:
        list_o.append(i)
if len(list_z)>len(list_o):
    otvet=f'Nado perevernyt {len(list_z)} monetok!'
elif len(list_z)<len(list_o):
    otvet=f'Nado perevernyt {len(list_o)} monetok!'
else:
    rnd_list=list_z,list_o
    otvet=f'Nado perevernyt {len(rnc(rnd_list))} monetok!'
#print(spisok,list_z,list_o)
print(otvet)