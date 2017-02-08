class Stack(object):

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):

    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.max_stack.peek() is None or item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        if self.stack.peek() == self.max_stack.peek():
            self.max_stack.pop()
        return self.stack.pop()

    def get_max(self):
        """get max num from a stack

        >>> a = MaxStack()
        >>> a.push(5)
        >>> a.push(9)
        >>> a.push(11)
        >>> a.push(1)
        >>> print a.get_max()
        11

        >>> a = MaxStack()
        >>> print a.get_max()
        None

        >>> a = MaxStack()
        >>> a.push(0)
        >>> a.push(0)
        >>> a.push(-1)
        >>> print a.get_max()
        0
        """
        return self.max_stack.peek()

if __name__ == "__main__":
    import doctest
    doctest.testmod()



