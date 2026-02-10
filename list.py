from shared import *


def mk_list(*range_args) -> list[Number]:
    return list(range(*range_args))


def bSearchIter(sorted: list[Number], searchValue: Number) -> int:
    "returns the index of `searchValue`, or the index of its closest value if it doesn't exist"
    i_max = len(sorted)
    i_min = 0
    i_mid = ceil(i_max / 2)

    while searchValue != sorted[i_mid] and i_max - i_min > 1:
        # _v = sorted[i_mid]
        if searchValue < sorted[i_mid]:
            i_max = i_mid
        else:
            i_min = i_mid

        i_mid = ceil((i_max + i_min) / 2)

    if searchValue < sorted[i_mid]:
        return i_mid - 1
    else:
        return i_mid


def bSearchRec(sorted: list[Number], searchValue: Number) -> int:
    "returns the index of `searchValue`, or the index of its closest value if it doesn't exist"
    n = len(sorted)
    if n == 1:
        return 0
    i_mid = ceil(n / 2)
    if searchValue < sorted[i_mid]:
        return 0 + bSearchRec(sorted[0:i_mid], searchValue)
    else:
        return i_mid + bSearchRec(sorted[i_mid:n], searchValue)


def lshift(lst: list, i_min: int, i_max: int):
    # print(lst)
    _v = lst[i_min]
    for i in range(i_min, i_max):
        lst[i] = lst[i + 1]

    lst[i_max] = _v
    print(lst)


def rshift(lst: list, i_min: int, i_max: int):
    # print(lst)
    _v = lst[i_max]
    for i in range(i_max, i_min, -1):
        lst[i] = lst[i - 1]

    lst[i_min] = _v
    # print(lst)


def is_sorted_debug(lst):
    wrogn = []
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            wrogn.append(i)
    return wrogn if wrogn else "no way it work"


def bSort_(lst: list[Number]):
    n = len(lst)
    if n <= 1:
        return
    for idx in range(1, n):
        value = lst[idx]
        # binary search
        i_min = 0
        i_max = idx
        i_mid = ceil(i_max / 2)
        while i_max - i_min > 1 and value != lst[i_mid]:
            if value < lst[i_mid]:
                i_max = i_mid
            else:
                i_min = i_mid
            
            i_mid = ceil((i_max + i_min) / 2)

            # _half = (i_max + i_min) / 2

            # i_mid2 = (i_max + i_min) // 2

        # i_mid = i_mid if value < lst[i_mid] else i_mid+1
        # if i_min == 1:
        #     i_min = 0
        # shift
        for i in range(idx, i_mid, -1):
            lst[i] = lst[i - 1]

        # insert
        lst[i_mid] = value
        print(idx, lst[0:idx])
        # rshift(lst, i_mid, idx)

        # lst[i_mid:idx] = []
    # tmp = lst[0]
    # lst[-1] = lst[0]
    # lst[0] = tmp


from random import randint


def is_lst_eq(a: list, b: list):
    return all(x == y for x, y in zip(a, b))


def mk_list_rnd(size: int) -> list[Number]:
    return [randint(-30, 30) for _ in range(size)]


if __name__ == "__main__":
    lst = mk_list_rnd(20)
    shuffle(lst)
    print(lst)
    # print(2, 5, lst[2:5], lst[2], lst[5])
    # lshift(lst, 2, 5)
    # print()
    # rshift(lst, 2, 5)
    # print(lst)
    bSort_(lst)

    _l = sorted(lst)
    print(".sort:", _l)
    print("bSort:", lst)
    print(set(lst) == set(_l), is_lst_eq(lst, _l), is_sorted_debug(lst))

    # search = -2

    # i_rec = bSearchRec(lst, search)
    # i_iter = bSearchIter(lst, search)

    # print(lst,end="\n\n")
    # print("search:", search, end="\n\n")
    # print("iteritivly:")
    # print(f"found: i={i_iter}, v={lst[i_iter]}")

    # print("\nrecursive:")

    # print("search:", search)
    # print(f"found: i={i_rec}, v={lst[i_rec]}")
