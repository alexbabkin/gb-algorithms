"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
"""
import random


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array

    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])

    n = m = k = 0

    current = [0] * (len(left) + len(right))
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            current[k] = left[n]
            n += 1
        else:
            current[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        current[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        current[k] = right[m]
        m += 1
        k += 1
    for i in range(len(array)):
        array[i] = current[i]
    return array


size = 10
array = list(range(size))
random.shuffle(array)
print(array)


print(merge_sort(array))
