import csv #текстовый формат, предназначенный для представления табличных данных.
s=0
with open('products1.csv',newline=" ") as file:
    reader= csv.reader(file) #читаем файл
    print('Нужно купить:')
    next(reader) #возвращает следующую строку объекта чтения
    for row in reader: #пробегаемся по строкам
        print(row[0] + " - " + row[1] + " шт." + " за " + row[2] + ' руб.')
        s= s+ int(row[1])*int(row[2])
    print('Итоговая сумма:' + str(s) + 'руб.')
