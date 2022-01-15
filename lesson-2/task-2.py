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
