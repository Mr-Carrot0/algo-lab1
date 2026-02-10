from linkedlist import *
from shared import *


def mk_list(*range_args) -> list[Number]:
    return list(range(*range_args))


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


def bSearchLL(search_value: Number, head: NodeLL, n: int) -> NodeLL | int:
    # """returns the refrence of the `NodeLL` where `search_value` sould be inserted,
    # returning None if it should be `push_front`'d"""
    # if n is None:
    #     n = len(sorted)
    # curr = sorted.head

    if n == 1:
        if search_value < head.value:
            return -1
        else:
            return head
    if n == 2:
        if search_value < head.value:
            return head
        else:
            return -1

    n_half = ceil(n / 2)

    mid = LinkedList.advance(head, n_half)

    assert mid != None

    # ins_v = LinkedList.pop_next(mid_prev)
    if search_value == mid.value:
        return mid
    elif search_value < mid.value:
        return bSearchLL(search_value, head, n_half)
    elif search_value > mid.value:
        return bSearchLL(search_value, mid, n_half)


# def bSortLL(lst: LinkedList):
#     prev = lst.head
#     # for i in range(len(lst)):


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
    # for i in range(-5, 50, 2):
    #     _t = bSearchLL(i, ll.head, n - 1)
    #     # assert _t is not None
    #     if not isinstance(_t, NodeLL):
    #         print("_t:",_t, i)
    #     else:
    #         # print(_t)
    #         # if i > _t.next.value:
    #         print(
    #             _t.value,
    #             i,
    #             # _t.value <= i,
    #             # _t.value <= i,
    #             end=" ",
    #         )
    #         print(_t.next.value if _t.next is not None else "")
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
