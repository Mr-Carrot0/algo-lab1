from shared import *
from math import ceil, floor


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


def bSearchLL(search_value: Number, head: NodeLL, n: int) -> NodeLL | None:
    # """returns the refrence of the `NodeLL` where `search_value` sould be inserted,
    # returning None if it should be `push_front`'d"""
    # if n is None:
    #     n = len(sorted)
    # curr = sorted.head

    if n <= 2:
        if search_value < head.value:
            return None
        else:
            return head

    n_half = n // 2

    mid_prev = LinkedList.advance(head, n_half)

    assert mid_prev.next != None

    # ins_v = LinkedList.pop_next(mid_prev)
    if search_value == mid_prev.value:
        return mid_prev
    elif search_value < mid_prev.value:
        return bSearchLL(search_value, head, n - n_half)
    elif search_value > mid_prev.value:
        return bSearchLL(search_value, mid_prev, n - n_half)


def bSortLL(lst: LinkedList):
    prev = lst.head
    # for i in range(len(lst)):


from random import shuffle

if __name__ == "__main__":
    # for i in range(1, 20):
    #     print(f"{i}:\t {i//2-1}")
    lst = mk_list(30)
    n = len(lst)
    ll = LinkedList(*lst)

    # print(LinkedList.advance(ll.head,9))

    print(len(lst), lst)
    print(len(ll), ll)

    # # print(LinkedList.advance())
    for i in range(0, 50, 2):
        _t = bSearchLL(i, ll.head, n)
        assert _t is not None
        # print(_t)
        if i > _t.next.value:
            print(
                _t.value,
                i,
                _t.next.value,
                # _t.value <= i,
                # _t.value <= i,
            )
        # print()
    # shuffle(lst)
    # print("len(lst)=", len(lst))

    # best_i = bSearchList(5, lst)
    # print(best_i)
    # print(lst[best_i])

# def bSortList(value, lst: list[Number]):
#     for i, value in enumerate(lst):
#         best_i = bSearchList(value, lst[:i])


# m = LinkedList(*mk_list(100))

# print(repr(m))
# print(curr)

# print(mk_list(6))
# from timeit import timeit

# size = 1000
# l = mk_list(size)

# print("timer:")
# t = timeit("bSearchList(7, l)", globals=locals())
# print(t)
