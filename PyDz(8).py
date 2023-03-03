from random import randint as rnd
print('Vvedite N : ')
N_num = int(input())
spisok = []
for i in range(N_num):
    spisok.append(rnd(0,N_num))
print(spisok)
print('Vvedite X : ')
X_num = int(input())
count = 0
for i in spisok:
    if i == X_num:
        count += 1
print(count)