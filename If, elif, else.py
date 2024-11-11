number1 = input('Введите первое число ')
number2 = input('Введите второе число ')
number3 = input('Введите третье число ')
print('Количество одинаковых чисел:')
if number1 == number2 == number3:
    print(3)
elif number1 == number2 or number1 == number3 or number2 == number3:
    print(2)
else:
    print(0)
