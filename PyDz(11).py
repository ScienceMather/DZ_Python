nabor_1 = set(input("Vvedite spisok 1: "))
nabor_2 = set(input("Vvedite spisok 2: "))
nabor_3 = nabor_1.intersection(nabor_2)
nabor_3.discard(' ')
print(sorted(list(nabor_3)))