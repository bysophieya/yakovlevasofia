import random
k=0
spisok=['Киселева',"Байол","Столярова","Емельянова","Киреева","Яковлева","Пискунова","Овчинникова","Чугунова","Зубцова"]
spisok2=["Савинова","Гончарова","Иванов","Мельникова","Величко","Стрельцова","Терентьева","Гребенщиков","Шишкина","Овсянко"]
team = tuple(random.sample(spisok, 5)+random.sample(spisok2, 5)) #выбираем по 5 рандомных людей из 2 списков
print('Студенты моей группы ',spisok)
print('Студенты другой группы ',spisok2)
print('Спортивная команда ',team)
print('Длина кортежа ',len(team))
team = tuple(sorted(team)) #сортируем по алфавиту
print('Отсортированный список ',team)
if 'Иванов' in team:
    k+=1
    print('В команду входит Иванов',k,'раз')
else:
    print('Иванов в команду не входит ')
