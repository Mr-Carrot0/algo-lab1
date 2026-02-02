def mk_list(*range_args):
    return list(range(*range_args))


class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next: NodeLL | None = None

    def __repr__(self):
        return f"NodeLL({self.data},{ "" if self.next is None else " ..."})"


class LinkedList:
    head: NodeLL

    def __init__(self, *args):
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

    def print(self):
        self.forEach(print)

    def __repr__(self):
        s = "LinkedList["
        curr: NodeLL | None = self.head
        while curr is not None:
            s += repr(curr.data) + ", "
            curr = curr.next
        s = s.strip(", ")
        return s + "]"
