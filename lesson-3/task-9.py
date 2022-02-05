# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

lines_count = 4
columns_count = 5

matrix = [[random.randint(1, 10) for _ in range(columns_count)]
          for _ in range(lines_count)]

print('Исходная матрица:')
print('=' * 25)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print('')

print('=' * 25)

max = 0

for i in range(columns_count):
    min_from_column = 10

    for j in range(lines_count):
        if min_from_column > matrix[j][i]:
            min_from_column = matrix[j][i]
    print(f'Минимальный элемент столбца {i + 1}: {min_from_column}')

    if min_from_column > max:
        max = min_from_column

print('=' * 25)
print(f'Максимальный элемент: {max}')
