#
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#

number = int(input("ведите число: "))

even_num, odd_num = 0, 0

# 0 - тоже чилсо
while True:
    d = number % 10

    if d % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

    number //= 10

    if number == 0:
        break


print(f"Четных цифр: {even_num}")
print(f"Нечетных цифр: {odd_num}")
