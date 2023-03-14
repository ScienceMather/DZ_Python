first_elem = int(input("Vvedite pervoe chislo: "))
differ = int(input("Vvedite raznost: "))
amount = int(input("Vvedite chislo elementov: "))
arifm_progres=[]
for i in range(1,amount + 1):
    an = first_elem + (i-1) * differ
    arifm_progres.append(an)
print(arifm_progres)