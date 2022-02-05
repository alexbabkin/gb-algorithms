#
#  В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
#

from random import randint

a = [randint(0, 20) for _ in range(10)]
print(f"Исходный массив: {a}")

min1, min2 = a[0], a[1]

for elem in a:
    if elem < min1:
        min1 = elem
    elif elem < min2:
        min2 = elem

print(min1, min2)
