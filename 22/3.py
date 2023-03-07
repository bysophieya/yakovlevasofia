word=input('Введите слово  ')
k=0
for i in range(0,len(word)):
    if (word[i] =='ф') or (word[i] == 'Ф'):
        k= k+1
if k >= 1:
    print('Ого!Это редкое слово!')
else:
    print('Эх, это не очень редкое слово...')
