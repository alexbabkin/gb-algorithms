while True:
    operation = input("введите операцию: ")
    if operation == "0":
        break
    if operation == "+" or operation == "-" or operation == "/" or operation == "*":
        op1 = float(input("введите первый операнд: "))
        op2 = float(input("введите второй операнд: "))
        if operation == "+":
            print(f"Результат: {op1 + op2}")
        elif operation == "-":
            print(f"Результат: {op1 - op2}")
        elif operation == "*":
            print(f"Результат: {op1 * op2}")
        elif operation == "/":
            if op2 == 0.0:
                print("Нельзя делить на ноль")
            else:
                print(f"Результат: {op1 / op2}")
    else:
        print("неверная операция, попробуйте еще раз")
