n = int(input("Введите n: "))

sum = 0
for i in range(n):
    sum += i + 1

is_eq = sum == n * (n + 1) / 2
print(is_eq)
