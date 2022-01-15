number = int(input("ведите число: "))

_reversed = 0

# 0 - тоже чилсо
while True:
    _reversed *= 10
    remainder = number % 10
    _reversed += remainder

    number //= 10

    if number == 0:
        break

print(f"Обратное: {_reversed}")
