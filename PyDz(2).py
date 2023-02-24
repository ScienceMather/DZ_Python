print('Vvedite chislo: ')
chisllo = int(input())
if chisllo%4==0:
    chisllo1=chisllo//2
    chisllo2=chisllo1//2
    print(chisllo2,chisllo1,chisllo2)
else:
    print('Nevernoe chislo!')
