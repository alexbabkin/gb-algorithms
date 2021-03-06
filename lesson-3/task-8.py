
# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = [[int(input(f"{j}:{i} Число: ")) for i in range(5)] for j in range(4)]

for line in matrix:
    sum_line = 0
    for item in line:
        sum_line += item
        print(f'{item:>5}', end='')
    print(f'   | {sum_line}')
