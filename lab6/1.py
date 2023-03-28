countries={"Россия":"Москва","Германия":"Берлин","Франция":"Париж","Норвегия":"Осло","Италия":"Рим"}
for key in countries:
    print(key,'-',countries[key]) #выводим на экран все пары ключ-значение
stoliza=input("Введите страну:")
user=countries.get(stoliza) # получаем столицу для страны
print(user)
list_keys = list(countries.keys())
list_keys.sort() #сортируем страны по алфавиту
for i in list_keys:
    print(i, ':', countries[i])
