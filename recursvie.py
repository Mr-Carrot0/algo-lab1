from linkedlist import *
from math import ceil




# def bSearchLL(head: NodeLL, search_value: number, max_rel: int):
#     max_rel_d2 = ceil(max_rel / 2) - 1
#     if max_rel_d2 <= 1:
#         return head

#     mid: NodeLL = advance(head, max_rel_d2)  # O(max_rel/2)

#     if search_value == mid.value:
#         return mid
#     elif search_value > mid.value:
#         return bSearchLL(mid, search_value, max_rel_d2)
#     elif search_value < mid.value:
#         return bSearchLL(head, search_value, max_rel_d2)

#     raise Exception("scenario not accounted for in recursvive bSearchLL")


# def bSortLL(lst: LinkedList):
#     curr = lst.head
#     prev = None
#     # i = 0
#     for i in range(len(lst)):
#         # print(i)
#         print(curr.value)
#         best_prev_ptr = bSearchLL(lst.head, curr.value, i)

#         if prev is not None:  # not first iter
#             if best_prev_ptr is not prev:


#                 prev.next = curr.next

#                 curr.next = best_prev_ptr.next

#             best_prev_ptr.next = curr

#             curr = prev.next

#         else:
#             curr = curr.next

#         prev = curr
#         # i += 1
#     # mid = advance(head, max_rel)


# if __name__ == "__main__":
    # l = LinkedList(4, 7, 1, 2)
    # print(l)
    # print(len(l))
    # bSortLL(l)
    # print(l)
    
