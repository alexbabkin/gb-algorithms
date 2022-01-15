#
# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
#

alphabet = 'abcdefghijklmnopqrstuywxyz'

letter_1 = input('Введите первую букву: ')
letter_2 = input('Введите вторую букву: ')
letter_1_idx = alphabet.index(letter_1) + 1
letter_2_idx = alphabet.index(letter_2) + 1

print(f'Позиция первой буквы: {letter_1_idx}')
print(f'Позиция второй буквы: {letter_2_idx}')
print(
    f'Между ними {abs(letter_2_idx - letter_1_idx) - 1 if letter_1_idx != letter_2_idx else 0} символа')
