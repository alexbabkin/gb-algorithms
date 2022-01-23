#
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#

from random import randint

a = [randint(0, 20) for _ in range(10)]

print(f"Исходный массив: {a}")

min_idx = max_idx = 0
for idx in range(len(a)):
    if a[idx] > a[max_idx]:
        max_idx = idx
    if a[idx] < a[min_idx]:
        min_idx = idx

a[min_idx], a[max_idx] = a[max_idx], a[min_idx]

print(f"С поменянными макс и мин элементами: {a}")
