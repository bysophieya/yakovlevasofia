def bilet(number):
    half = len(number) // 2
    half1 = number[:half]
    half2 = number[half:]
    if sum(map(int, half1)) == sum(map(int, half2)):
        return True
    else:
        return False
number=input('Введите номер билета ')
if len(number) % 2 == 0:
    result=bilet(number)
    if result == True:
        print("Поздравляем! У вас счастливый билет!")
    else:
        print("К сожалению у вас несчастливый билет ")
else:
    print("Количество цифр билета нечетно")