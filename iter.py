from shared import *
from math import ceil
from random import randint


def bSearchList(value, sorted: list[int | float]) -> int:
    i_max = len(sorted)
    i_min = 0
    i_mid = ceil(i_max / 2)

    while value != sorted[i_mid] and i_max - i_min > 1:
        if value < sorted[i_mid]:
            i_max = i_mid
        else:
            i_min = i_mid

        i_mid = ceil((i_max + i_min) / 2)

    if value == sorted[i_mid]:
        return i_mid
    else:
        # not in list
        return -1

def bSortList(value, sorted: list[int | float]) -> int:
    pass


# m = LinkedList(*mk_list(100))

# print(repr(m))
# print(curr)

# print(mk_list(6))
from timeit import timeit

size = 1000
l = mk_list(size)

print("timer:")
t = timeit("bSearchList(7, l)", globals=locals())
print(t)
