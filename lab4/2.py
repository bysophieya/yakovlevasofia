def delenie(x):
    try:
        return 100 / x
    except ZeroDivisionError:
        print('Ошибка ! Деление на ноль !')
        return None
num1=input('Введите число ')
try:
    num2=int(num1)
except ValueError:
    print("Ошибка!Вы ввели не число !")
else:
    result=delenie(num2)
    if result is not None:
        print(result)