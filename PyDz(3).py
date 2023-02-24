print('Vvedite chislo 6 znakov: ')
chisllo = int(input())
firsttrio=chisllo//100000%10+chisllo//10000%10+chisllo//1000%10
secondtrio=chisllo//100%10+chisllo//10%10+chisllo%10
if firsttrio == secondtrio:
    print("Bilet schaslivii!")
else:
    print("Bilet ne schaslivii!")