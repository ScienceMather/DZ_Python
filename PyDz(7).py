print('Vvedite chislo : ')
chislo=int(input())
num_list=[]
for i in range(100):
    if 2**i<chislo:
         num_list.append(2**i)
print(num_list)