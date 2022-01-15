#
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
#

alphabet = 'abcdefghijklmnopqrstuywxyz'

idx = int(input('Введите номер буквы (от 1 до 26): '))
letter = alphabet[idx - 1]
print(f'Это буква: {letter}')
