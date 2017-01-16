class Queue():
    """implement a queue using two stacks"""
    def __init__(self):
        self._queue = []

    def __repr__(self):
        return str(self._queue)

    def enqueue(self, num):
        """add a number to the queue
        """
        self._queue.append(num)

    def dequeue(self):
        """pop a number off the front of the queue
        """
        first_item = self._queue[0]
        self._queue.remove(first_item)


if __name__ == "__main__":
    import doctest
    doctest.testmod()