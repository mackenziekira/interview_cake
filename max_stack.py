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


class MaxStack(Stack):

    def __init__(self):
        super(MaxStack, self).__init__()

    def get_max(self):
        """get max num from a stack

        """
        max_item = None

        for item in self.items:
            if item > max_item:
                max_item = item

        return max_item

a = MaxStack()
a.push(5)
a.push(9)
a.push(11)
a.push(1)
print a.get_max()



