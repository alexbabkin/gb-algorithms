#
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#

# я предполагаю, что максимальный отрицательный, это тот, который ближе к нулю с левой стороны на числовой оси

from random import randint

a = [randint(-10, 10) for _ in range(10)]
print(f"Исходный массив: {a}")

max_negative, max_negative_idx = None, None
for idx in range(len(a)):
    elem = a[idx]
    if elem < 0:
        if max_negative is None:
            max_negative, max_negative_idx = elem, idx
        elif -elem < -max_negative:
            max_negative, max_negative_idx = elem, idx


print(f"Максимальный отрицательный элемент: {max_negative}, его индекс: {idx}")
