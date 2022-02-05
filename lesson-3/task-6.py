#
#  В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#   Сами минимальный и максимальный элементы в сумму не включать.
#
# В соотетствии с заданием не будем использовать min и max и их самописные аналоги
#

from random import randint

a = [randint(0, 20) for _ in range(10)]
print(f"Исходный массив: {a}")

min_elem, max_elem = None, None

# пока что предположим, что сначала идет минимальный, а потом максимальный элемииенты
s, sum_after_max = 0, 0
max_elem, min_elem = a[0], a[0] + 1

for elem in a:
    # пока суммируем все подряд
    s += elem
    if elem < max_elem:
        # Все, что после максимума, мы вычтем в конце
        sum_after_max += elem
    else:
        # если встретили новый максимум, то обнуляем сумму после максимума
        max_elem, sum_after_max = elem, elem
    if elem < min_elem:
        # нам не интересно, все что до минимума, обнуляем сумму
        s, min_elem = 0, elem
# вычитаем сумму после максимума
s -= sum_after_max

if s >= 0:
    print(f"Сумма = {s}, между ({min_elem} и {max_elem})")
else:
    # оказалось, что сначала идет максимум, а потом минимум.
    # Но у нас уже есть минимальный и максимальный элементы, тут все проще
    meat_max, s = False, 0
    for elem in a:
        if meat_max:
            if elem == min_elem:
                break
            s += elem
        if elem == max_elem:
            meat_max = True

    print(f"Сумма = {s}, между ({max_elem} и {min_elem})")
