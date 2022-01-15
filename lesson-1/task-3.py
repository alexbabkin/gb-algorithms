#
# Написать программу, которая генерирует в указанных пользователем границах:
#  a. случайное целое число,
#  b. случайное вещественное число,
#  c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
#

import random

# целые числа
min_int = int(input('Введите начало диапазона (целые): '))
max_int = int(input('Введите конец диапазона (целые): '))

random_int = random.randint(min_int, max_int)
print(f'Случайное целое [{min_int}, {max_int}]: {random_int}')

min_float = float(input('Введите начало диапазона (вещественные): '))
max_float = float(input('Введите конец диапазона (вещественные): '))

random_float = random.uniform(min_float, max_float)
print(f'Случайное вещественное [{min_float}, {max_float}]: {random_float}')

# буквы
alphabet = 'abcdefghijklmnopqrstuywxyz'

min_letter = input('Введите начало диапазона (буквы): ')
max_letter = input('Введите конец диапазона (буквы): ')
min_letter_idx = alphabet.index(min_letter)
max_letter_idx = alphabet.index(max_letter)


random_letter_idx = random.randint(
    min_letter_idx, max_letter_idx)
random_letter = alphabet[random_letter_idx]
print(
    f'Случайная буква [{min_letter}({min_letter_idx}), {max_letter}({max_letter_idx})]: {random_letter}({random_letter_idx})')
