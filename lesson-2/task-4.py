#
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
#

count = int(input("ведите количество членов ряда: "))

coeff = 1
result = 0
for i in range(count):
    elem = coeff / 2 ** i
    result += elem if i % 2 == 0 else -elem

print(f"Сумма = {result}")
