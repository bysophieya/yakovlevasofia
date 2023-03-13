def data():
    day = int(input('Введите день '))
    month = int(input('Введите месяц '))
    year = int(input('Введите год '))
    year1 = year % 100
    if day * month == year1:
        return True
    else:
        return False
print(data())
