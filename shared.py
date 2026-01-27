def mk_list(*range_args):
    return list(range(*range_args))


class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"NodeLL({self.data},{ "" if self.next is None else " ..."})"


class LinkedList:
    head: NodeLL

    def __init__(self, *args):
        _b = True
        prev: NodeLL = None
        for v in args:
            if _b:
                _b = False
                prev = self.head = NodeLL(args[0])
            else:
                prev.next = NodeLL(v)
                prev = prev.next

    def forEach(self, fn):
        curr: NodeLL = self.head
        while curr:
            fn(curr)
            curr = curr.next

    def print(self):
        self.forEach(print)

    def __repr__(self):
        s = "LinkedList["
        curr: NodeLL = self.head
        while curr:
            s += repr(curr.data) + ", "
            curr = curr.next
        s = s.strip(", ")
        return s + "]"
