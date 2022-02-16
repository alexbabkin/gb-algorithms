"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и
определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением
будет:
a.  выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b.  написать 3 варианта кода (один у вас уже есть);
    проанализировать 3 варианта и выбрать оптимальный;
c.  результаты анализа (количество занятой памяти в вашей среде разработки)
    вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d.  написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof
после каждой переменной, а проявили творчество, фантазию и создали
универсальный код для замера памяти.

Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

import sys


def show_sizeof(x, memory_list, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    memory_list.append(sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_sizeof(key, memory_list, level + 1)
                show_sizeof(value, memory_list, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_sizeof(item, memory_list, level + 1)


def mem_size(variables):
    sum_mem = 0
    for obj in variables:
        mem_list = []
        if obj.startswith('__'):
            continue
        elif hasattr(variables[obj], '__call__'):
            continue
        elif hasattr(variables[obj], '__loader__'):
            continue
        else:
            show_sizeof(variables[obj], mem_list)
            for item in mem_list:
                sum_mem += item
    return f'Суммарная память: {sum_mem} байт'


def sum1(n_elements):
    element = 1
    res = element
    for _ in range(1, n_elements):
        element /= -2
        res += element
    return res, locals()


def sum2(n_elements):
    row = [1, ]
    res = row[0]

    for i in range(1, n_elements):
        row.append(row[i - 1] / -2)
        res = res + row[i]

    return res, locals()


def sum3(n_elements):
    res = 1 * (1 - (-0.5) ** n_elements) / (1 - (-0.5))
    return res, locals()


def print_res(s, variables):
    print(f'Сумма равна: {s}. Требуемая память: {mem_size(variables)}')


number_of_elements = int(input("Input n: "))

print('-----------Вариант 1-----------')
print_res(*sum1(number_of_elements))

print('-----------Вариант 2-----------')
print_res(*sum2(number_of_elements))

print('-----------Вариант 3-----------')
print_res(*sum3(number_of_elements))


"""
Input n: 5
-----------Вариант 1-----------
 <class 'int'> 28 5
 <class 'float'> 24 0.0625
 <class 'float'> 24 0.6875
 <class 'int'> 28 4
Сумма равна: 0.6875. Требуемая память: Суммарная память: 104 байт
-----------Вариант 2-----------
 <class 'int'> 28 5
 <class 'list'> 120 [1, -0.5, 0.25, -0.125, 0.0625]
         <class 'int'> 28 1
         <class 'float'> 24 -0.5
         <class 'float'> 24 0.25
         <class 'float'> 24 -0.125
         <class 'float'> 24 0.0625
 <class 'float'> 24 0.6875
 <class 'int'> 28 4
Сумма равна: 0.6875. Требуемая память: Суммарная память: 324 байт
-----------Вариант 3-----------
 <class 'int'> 28 5
 <class 'float'> 24 0.6875
Сумма равна: 0.6875. Требуемая память: Суммарная память: 52 байт

Лучшим оказался третий вариант, он не требует дополнительных переменных, а использует готовую формулу
"""

# ОС: Windows 10 64-bit
# Python 3.10.2
