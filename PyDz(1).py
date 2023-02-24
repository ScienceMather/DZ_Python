print('Vvedite trehznachnoe chislo: ')
chisllo = int(input())
chisllo1= chisllo%10
print('c1',chisllo1)
chisllo2= ((chisllo-chisllo1)//10)%10
print('c2',chisllo2)
chisllo3= (((chisllo-chisllo1)//10)//10)%10
print('c3',chisllo3)
otvet=chisllo1+chisllo2+chisllo3
print(otvet)
