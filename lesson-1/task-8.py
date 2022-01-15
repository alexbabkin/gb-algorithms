#
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
#

numb_1 = float(input('Введите первое число: '))
numb_2 = float(input('Введите второе число: '))
numb_3 = float(input('Введите третье число: '))

if numb_1 <= numb_2 <= numb_3:
    print(f'{numb_2} - среднее')
elif numb_2 <= numb_1 <= numb_3:
    print(f'{numb_1} - среднее')
else:
    print(f'{numb_3} - среднее')
