from random import shuffle as shf
print('Vvedite N : ')
N_num = int(input())
spisok = []
for i in range(N_num):
    spisok.append(i)
shf(spisok)
print(spisok)
print('Vvedite X : ')
X_num = int(input())
diff = N_num
srch_num = None
for i in spisok:
    if abs(i-X_num)<diff:
        diff = abs(i-X_num)
        srch_num = i
print(srch_num)
