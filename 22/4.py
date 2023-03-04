c=0
k=0
k1=0
for i in range(1,8):
    for j in range(1,5):
        print( i,"+",j,"= ",end="")
        otvet = int(input())
        c = i + j
        if otvet == c:
            print('Правильно!')
            k+=1
        else:
            print('Ответ неверный.')
            k1+=1
        if k1==3:
            print('Игра окончена.Правильных ответов:', k)
            exit()
