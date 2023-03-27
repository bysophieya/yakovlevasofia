countries={"Россия":"Москва","Германия":"Берлин","Франция":"Париж","Норвегия":"Осло","Италия":"Рим"}
for key in countries:
    print(key,'-',countries[key])
stoliza=input("Введите страну:")
user=countries.get(stoliza)
print(user)
list_keys = list(countries.keys())
list_keys.sort()
for i in list_keys:
    print(i, ':', countries[i])