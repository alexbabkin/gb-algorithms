#
# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.
#


x1 = float(input('Введите координату x первой точки: '))
y1 = float(input('Введите координату y первой точки: '))
x2 = float(input('Введите координату x второй точки: '))
y2 = float(input('Введите координату y второй точки: '))

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

if k != 0.0:
    if b > 0.0:
        print(f'y = {round(k, 3)}x + {round(b, 3)}')
    elif b == 0.0:
        print(f'y = {round(k, 3)}x')
    else:
        print(f'y = {round(k, 3)}x - {abs(round(b, 3))}')
else:
    print(f'y = {round(b, 3)}')
