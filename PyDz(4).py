print('Vvedite chislo n: ')
ch_n= int(input())
print('Vvedite chislo m: ')
ch_m = int(input())
print('Vvedite chislo k: ')
ch_k = int(input())
print('n= ',ch_n,',','m= ',ch_m,',','dolek= ',ch_k)
if ch_k%ch_n==0 or ch_k%ch_m==0:
    print('k dolek mojno vzyat')
else:
    print('k dolek nelzya vzyat')