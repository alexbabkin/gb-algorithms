"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

# для честности не будем использовать встроенные min и max


def find_max(array):
    m = array[0]
    for i in range(1, len(array)):
        if array[i] > m:
            m = array[i]
    return m


def find_min(array):
    m = array[0]
    for i in range(1, len(array)):
        if array[i] < m:
            m = array[i]
    return m


def remove_max_min(array):
    array.remove(find_max(array))
    array.remove(find_min(array))


def find_median(array):
    while(len(array) != 1):
        remove_max_min(array)
    return array[0]


m = 10
# нечетное чилсо элементов
size = 2 * m + 1
array = list(range(size))
random.shuffle(array)
print(array)


print(find_median(array))
