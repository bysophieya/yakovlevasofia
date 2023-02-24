color1=input('Введите название основного цвета ')
color2=input('Введите название второго основного цвета ')
if (color1 != "красный" and color1 != "желтый" and color1 != "синий") or (color2 != "красный" and color2 != "желтый" and color2 != "синий"):
    print('Вы ввели не основной цвет')
if color1 == "красный" and color2 == "синий":
    print("получается фиолетовый")
elif color1 == "красный" and color2 == "желтый":
    print("получается оранжевый")
elif color1 == "синий" and color2 == "желтый":
    print("получается зеленый")
