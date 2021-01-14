from code_challenges.stacks_and_queues.stacks_and_queues import (
    Stack,
    InvalidOperationError,
)


class PseudoQueue:
    def __init__(self):
        self.first_on_top = Stack()
        self.last_on_top = Stack()

    def enqueue(self, value):
        while not self.first_on_top.is_empty():
            self.last_on_top.push(self.first_on_top.pop())

        self.last_on_top.push(value)

    def dequeue(self):

        while not self.last_on_top.is_empty():
            self.first_on_top.push(self.last_on_top.pop())

        if self.first_on_top.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.first_on_top.pop()
