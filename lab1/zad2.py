mesto=int(input('Введите номер места в вагоне'))
if mesto > 54:
    print('Такого места нет')
    exit()
if (0 < mesto <= 36):
    print('Ваше место в купе')
else:
    print('Ваше место боковое')
if mesto % 2 == 0:
    print('верхнее')
else:
    print('нижнее')

