# -*- coding: utf-8 -*-
"""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям 
(по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


def graph(size):
    return [
        [0 if item == line else 1 for item in range(size)]
        for line in range(size)]


def count(g):
    meta = g
    g = 0

    for i, line in enumerate(meta):
        for j, item in enumerate(line):
            if i < j:
                g += item

    return g


n = int(input("Количество друзей: "))
print(f'Количество руковожатий: {count(graph(n))}')
