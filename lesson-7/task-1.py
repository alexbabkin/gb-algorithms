"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). 
Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random


def bubble_sort(array):
    if len(array) == 0 or len(array) == 1:
        return
    i, to_be_continued = 0, True
    while(to_be_continued):
        to_be_continued = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                to_be_continued = True
        i += 1


size = 10
array = list(range(size))
random.shuffle(array)
print(array)

bubble_sort(array)
print(array)
