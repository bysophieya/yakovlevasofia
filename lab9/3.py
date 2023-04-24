import csv
s=0
with open('products1.csv',"r") as file:
    reader= csv.reader(file) #читаем файл
    print('Нужно купить:')
    next(reader)
    for row in reader:
        print(row[0] + " - " + row[1] + " шт." + " за " + row[2] + ' руб.')
        s= s+ int(row[1])*int(row[2])
    print('Итоговая сумма:' + str(s) + 'руб.')
