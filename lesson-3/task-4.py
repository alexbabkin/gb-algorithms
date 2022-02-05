#
# Определить, какое число в массиве встречается чаще всего.
#

from random import randint

a = [randint(0, 10) for _ in range(50)]
print(f"Исходный массив: {a}")

num_with_max_occ, occ_count = None, 0
result = {}
for elem in a:
    if result.get(elem) is None:
        result[elem] = 1
    else:
        result[elem] += 1

    if num_with_max_occ is None or result[elem] > num_with_max_occ:
        num_with_max_occ, occ_count = elem, result[elem]


print(f"Число {num_with_max_occ} встречается чаще всего ({occ_count} раз(а))")
