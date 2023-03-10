num_a = int(input("Vvedite A: "))
num_b = int(input("Vvedite B: "))
def summ_rekyrs(na, nb):
    if nb == 0: 
        return 1
    else:
        return na + summ_rekyrs(1, nb - 1)        
print(summ_rekyrs(num_a, num_b))

