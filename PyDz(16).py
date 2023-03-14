from random import randint as rnd,randrange as rng,shuffle as shf

ind_list = []
rand_list = [rnd(-10,11) for _ in range(rnd(10,21))]
#rand_list = [rng(-10,11) for _ in range(rnd(10,21))]
shf(rand_list)
print(f"Dlina spiska ravna {len(rand_list)}!")
print(rand_list)
first_num = int(input("Vvedite pervoe chislo: "))
second_num = int(input("Vvedite vtoroe chislo: "))
for i in range(len(rand_list)):
    if first_num < rand_list[i] < (second_num + 1):
        ind_list.append(i)
print(ind_list)