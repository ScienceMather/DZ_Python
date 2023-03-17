stroka = str(input('Vvedite frazy: '))
format_stroka = stroka.split()
glas={'а', 'о', 'у', 'ы', 'э', 'я', 'ё', 'ю', 'и', 'е'}
count = 0
check_list = set()
for i  in format_stroka:
    count = 0
    for j  in i:
        if j in glas:
            count += 1
    check_list.add(count)
if len(check_list) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
#кашина-папаша машина-мама -> {6} -> "Парам пам-пам"
#пара-пам па-па-пам прам-пам-па пара-па -> "Парам пам-пам"
#кашина-папаша машина-мамаша -> {5, 6} -> "Пам парам"
#па пара ра пам-пар-па -> "Пам парам"