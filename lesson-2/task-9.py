#
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
#

def calc_digits_sum(number):
    res = 0
    while number > 0:
        d = number % 10
        res += d
        number //= 10
    return res


max_digits_sum, num = 0, 0
while True:
    user_in = input("введите следующее число (enter для завершения ввода): ")
    if user_in == "":
        break
    digits_sum = calc_digits_sum(int(user_in))
    if digits_sum > max_digits_sum:
        max_digits_sum = digits_sum
        num = int(user_in)


print(f"Максимальная сумма цифр {max_digits_sum} у числа {num}")
