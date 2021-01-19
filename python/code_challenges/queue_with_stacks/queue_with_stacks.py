from code_challenges.stacks_and_queues.stacks_and_queues import (
    Stack,
    InvalidOperationError,
)


class PseudoQueue:
    def __init__(self):
        """[Upon instantiation of a PseudoQueue class the class will create two empty stacks]"""
        self.first_on_top = Stack()
        self.last_on_top = Stack()

    def enqueue(self, value):
        """[Adds a node to the queue]

        Args:
            value ([type]): [value of the Node]
        """
        while not self.first_on_top.is_empty():
            self.last_on_top.push(self.first_on_top.pop())

        self.last_on_top.push(value)

    def dequeue(self):
        """[Removes a node from the queue]

        Raises:
            InvalidOperationError: [When you try to dequeue an empty PsuedoQueue]

        Returns:
            [type]: [returns the Node that was removed]
        """

        while not self.last_on_top.is_empty():
            self.first_on_top.push(self.last_on_top.pop())

        if self.first_on_top.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.first_on_top.pop()
