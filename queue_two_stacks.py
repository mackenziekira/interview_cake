class Stack(object):
    """a stack class"""
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return str(self.stack)

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

class Queue(object):
    """implement a queue using two stacks"""
    def __init__(self):
        self._instack = Stack()
        self._outstack = Stack()

    def __repr__(self):
        return str(self._instack) + str(self._outstack)

    def enqueue(self, num):
        """add a number to the queue
        """
        self._instack.push(num)

    def dequeue(self):
        """pop a number off the front of the queue
        """
        if self._outstack != []:
            return self._outstack.pop()

        while self._instack:
            self._outstack.push(self._instack.pop())

        return self._outstack.pop()


if __name__ == "__main__":
    import doctest
    doctest.testmod()