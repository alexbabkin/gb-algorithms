
def count_occurs(number, digit):
    res = 0
    while True:
        d = number % 10
        if d == digit:
            res += 1
        number //= 10

        if number == 0:
            return res


ocur_num = 0
digit = int(input("введите цифру: "))
while True:
    user_in = input("введите следующее число (enter для завершения ввода): ")
    if user_in == "":
        break
    ocur_num += count_occurs(int(user_in), digit)

print(f"{digit} встречается {ocur_num} раз(а)")
