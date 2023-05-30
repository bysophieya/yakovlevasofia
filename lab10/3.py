enru={}
with open('en-ru.txt','r') as file:
    for line in file:
        en , ru = line.strip().split(' - ')
        ru = ru.strip().split(', ')
        for i in ru:
            if i not in enru:
                enru[i]=[en]
            else:
                enru[i].append(en)
en_ru=sorted(enru.items())
print(enru)
with open('ru-en.txt',"w") as file:
    s=""
    for j in en_ru:
        s2=f'{j[0]} - {", ".join(i[1])}'
        s+= s2 + '\n'
    print(s)
    file.write(s)