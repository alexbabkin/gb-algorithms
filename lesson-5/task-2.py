"""
    2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
    При этом каждое число представляется как массив, элементы которого — цифры числа.
    Например, пользователь ввёл A2 и C4F. Нужно сохранить их как ["A", "2"] и ["C", "4", "F"] соответственно. 
    Сумма чисел из примера: ["C", "F", "1"], произведение - ["7", "C", "9", "F", "E"].
"""

from collections import deque
from copy import copy

hex_dec = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


def reverse_dict(d):
    return {v: k for k, v in d.items()}


dec_hex = reverse_dict(hex_dec)

num1 = deque(input("Ввведите первое число: "))
num2 = deque(input("Ввведите второе число: "))


def basic_sum(n1, n2):
    s = hex_dec[n1] + hex_dec[n2]
    if s > hex_dec["F"]:
        return dec_hex[s - 16], dec_hex[1]
    else:
        return dec_hex[s], dec_hex[0]


def hex_sum(num1, num2):
    num1, num2 = copy(num1), copy(num2)
    result = deque()
    additional_rank = "0"
    while(len(num1) > 0 or len(num2) > 0):
        n1 = num1.pop() if len(num1) > 0 else "0"
        n2 = num2.pop() if len(num2) > 0 else "0"
        s, a = basic_sum(n1, n2)
        if additional_rank != "0":
            if a != "0":
                s, _ = basic_sum(s, additional_rank)
            else:
                s, a = basic_sum(s, additional_rank)
        result.appendleft(s)
        additional_rank = a
    if additional_rank != "0":
        result.appendleft("1")
    return deque(result)


def basic_mul(n1, n2):
    res = deque("0")
    for _ in range(hex_dec[n2]):
        res = hex_sum(res, deque(n1))
    return res


def mul_num_n(num1, n2):
    num1 = copy(num1)
    result = deque()
    additional_rank = "0"
    while(len(num1) > 0):
        n1 = num1.pop()
        m = basic_mul(n1, n2)
        s = hex_sum(m, deque(additional_rank))
        result.appendleft(s.pop())
        if (len(s) > 0):
            additional_rank = s.pop()
        else:
            additional_rank = "0"
    if additional_rank != "0":
        result.appendleft(additional_rank)
    return result


def hex_mul(num1, num2):
    num1, num2 = copy(num1), copy(num2)
    muls_num_n = []
    current_runk = deque()
    while(len(num2) > 0):
        n2 = num2.pop()
        mul_num1_n2 = mul_num_n(num1, n2)
        mul_num1_n2.extend(current_runk)
        current_runk.append("0")
        muls_num_n.append(mul_num1_n2)
    res = deque("0")
    for a in muls_num_n:
        res = hex_sum(res, a)
    return res


print(hex_mul(num1, num2))
print(hex_sum(num1, num2))
