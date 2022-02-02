# -*- coding: utf-8 -*-

"""
1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания первых
 трех уроков.

    Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
    Например, если введено число 3486, надо вывести 6843.
"""
import cProfile


# цикл
def reverse1(number):
    _reversed = 0
    while True:
        _reversed *= 10
        remainder = number % 10
        _reversed += remainder

        number //= 10

        if number == 0:
            return _reversed


"""
python -m timeit -n 1000 -s "import task_1" "task_1.reverse1(123456789)"
1000 loops, best of 3: 1.91 usec per loop
python -m timeit -n 10000 -s "import task_1" "task_1.reverse1(123456789)"
10000 loops, best of 3: 1.88 usec per loop
python -m timeit -n 100000 -s "import task_1" "task_1.reverse1(123456789)"
100000 loops, best of 3: 1.96 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.reverse1(123456789123456789)"
1000 loops, best of 3: 3.96 usec per loop
python -m timeit -n 10000 -s "import task_1" "task_1.reverse1(123456789123456789)"
10000 loops, best of 3: 3.83 usec per loop
python -m timeit -n 100000 -s "import task_1" "task_1.reverse1(123456789123456789)"
100000 loops, best of 3: 3.83 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.reverse1(123456789123456789123456789)"
1000 loops, best of 3: 12.3 usec per loop
python -m timeit -n 10000 -s "import task_1" "task_1.reverse1(123456789123456789123456789)"
10000 loops, best of 3: 13 usec per loop
python -m timeit -n 100000 -s "import task_1" "task_1.reverse1(123456789123456789123456789)"
100000 loops, best of 3: 13.7 usec per loop

cProfile.run('[reverse1(123456789) for i in range(1000)]')
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1000    0.004    0.000    0.004    0.000 task_1.py:14(reverse1)

cProfile.run('[reverse1(123456789123456789) for i in range(1000)]')
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1000    0.006    0.000    0.006    0.000 task_1.py:14(reverse1)

cProfile.run('[reverse1(123456789123456789123456789) for i in range(1000)]')
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1000    0.015    0.000    0.015    0.000 task_1.py:14(reverse1)

Очевидно, что сложность алгоритма линейная, что логично, это один цикл
"""


# рекурсия
def reverse2(number, result=None):
    if number < 10:
        return result + number
    if result is None:
        result = 0
    result += number % 10
    return reverse2(number // 10, result * 10)


"""
python -m timeit -n 1000 -s "import task_1" "task_1.reverse2(123456789)"
1000 loops, best of 3: 2.4 usec per loop
python -m timeit -n 10000 -s "import task_1" "task_1.reverse2(123456789)"
10000 loops, best of 3: 2.64 usec per loop
python -m timeit -n 100000 -s "import task_1" "task_1.reverse2(123456789)"
100000 loops, best of 3: 2.31 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.reverse2(123456789123456789)"
1000 loops, best of 3: 4.73 usec per loop
python -m timeit -n 10000 -s "import task_1" "task_1.reverse2(123456789123456789)"
10000 loops, best of 3: 4.94 usec per loop
python -m timeit -n 100000 -s "import task_1" "task_1.reverse2(123456789123456789)"
100000 loops, best of 3: 5.02 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.reverse2(123456789123456789123456789)"
1000 loops, best of 3: 16.8 usec per loop
python -m timeit -n 10000 -s "import task_1" "task_1.reverse2(123456789123456789123456789)"
10000 loops, best of 3: 16.1 usec per loop
python -m timeit -n 100000 -s "import task_1" "task_1.reverse2(123456789123456789123456789)"
100000 loops, best of 3: 13.6 usec per loop

cProfile.run('[reverse2(123456789) for i in range(1000)]')
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
9000/1000    0.004    0.000    0.004    0.000 task_1.py:66(reverse2)

cProfile.run('[reverse2(123456789123456789) for i in range(1000)]')
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
8000/1000    0.009    0.000    0.009    0.000 task_1.py:66(reverse2)


cProfile.run('[reverse2(123456789123456789123456789) for i in range(1000)]')
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
27000/1000    0.031    0.000    0.031    0.000 task_1.py:66(reverse2)

Сложность отличается от линейной, вероятно O(nlog(n))
"""


# строка
def reverse3(number):
    return int(str(number)[::-1])


"""
python -m timeit -n 1000 -s "import task_1" "task_1.reverse3(123456789)"
1000 loops, best of 3: 1.13 usec per loop
python -m timeit -n 10000 -s "import task_1" "task_1.reverse3(123456789)"
10000 loops, best of 3: 1.33 usec per loop
python -m timeit -n 100000 -s "import task_1" "task_1.reverse3(123456789)"
100000 loops, best of 3: 0.909 usec per loop

python -m timeit -n 1000 -s "import task_1" "task_1.reverse3(123456789123456789)"
1000 loops, best of 3: 1.11 usec per loop
python -m timeit -n 10000 -s "import task_1" "task_1.reverse3(123456789123456789)"
10000 loops, best of 3: 1.53 usec per loop
python -m timeit -n 100000 -s "import task_1" "task_1.reverse3(123456789123456789)"
100000 loops, best of 3: 1.12 usec per loop


python -m timeit -n 1000 -s "import task_1" "task_1.reverse3(123456789123456789123456789)"
1000 loops, best of 3: 1.07 usec per loop
python -m timeit -n 10000 -s "import task_1" "task_1.reverse3(123456789123456789123456789)"
10000 loops, best of 3: 1.25 usec per loop
python -m timeit -n 100000 -s "import task_1" "task_1.reverse3(123456789123456789123456789)"
10000 loops, best of 3: 1.53 usec per loop

cProfile.run('[reverse3(123456789123456789123456789) for i in range(1000)]')
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1000    0.001    0.000    0.001    0.000 task_1.py:141(reverse3)

cProfile.run('[reverse3(123456789123456789123456789) for i in range(1000)]')
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1000    0.001    0.000    0.001    0.000 task_1.py:143(reverse3)

cProfile.run('[reverse3(123456789123456789123456789) for i in range(1000)]')
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1000    0.002    0.000    0.002    0.000 task_1.py:145(reverse3)

Сложность алгоритма меньше O(n), вероятно O(log(n))
"""
