stroka = str(input('Vvedite pari slov: '))
format_stroka = stroka.split()
kortej = []

#for i in format_stroka:
#    a = tuple(i.split('='))
#    kortej.append(a)
#print(tuple(kortej))

a = map((lambda i:tuple(i.split('='))),format_stroka)
kortej.append(a)
print(tuple(a))
