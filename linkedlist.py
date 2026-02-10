type Number = int | float

class NodeLL:
    def __init__(self, value: Number, next=None):
        self.value: Number = value
        self.next: NodeLL | None = next

    def __repr__(self):
        return f"NodeLL({self.value},{ "" if self.next is None else " ..."})"


class LinkedList:
    head: NodeLL

    def __init__(self, *args: Number):
        self.head = NodeLL(args[0])
        curr: NodeLL = self.head
        for _i, v in enumerate(args):
            match _i:
                case 0:
                    pass
                case _:
                    curr.next = NodeLL(v)
                    curr = curr.next

    def forEach(self, fn):
        curr: NodeLL | None = self.head
        while curr is not None:
            fn(curr)
            curr = curr.next

    def __len__(self):
        curr = self.head
        c = 0
        while curr is not None:
            c += 1
            curr = curr.next
        return c

    def push_front(self, value: Number):
        head = NodeLL(value, self.head)
        self.head = head

    def print(self):
        self.forEach(print)

    def __repr__(self):
        s = "LinkedList["
        curr: NodeLL | None = self.head
        while curr is not None:
            s += repr(curr.value) + ", "
            curr = curr.next
        # s = s.strip(", ")
        return s + "]"

    @staticmethod
    def pop_next(ptr: NodeLL):
        out = ptr.next

        ptr.next = ptr.next.next if ptr.next else None
        return out

    @staticmethod
    def insert_after(ptr: NodeLL, value: Number):
        _next = ptr.next
        ptr.next = NodeLL(value, _next)

    @staticmethod
    def advance(head: NodeLL, offset: int) -> NodeLL:
        curr = head
        if offset > 0:
            for _ in range(offset):
                curr = curr.next
                assert curr is not None
        return curr


# l = LinkedList(1, 4, 6, 89)
# print(l)
