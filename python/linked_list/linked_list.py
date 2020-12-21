class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    instances = 0

    def __init__(self, head, values=None):
        self.head = head
        LinkedList.instances +=1


    def insert(self, value):
        node = Node(value) # value 8 next None

        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self):
        pass

    @classmethod
    def ll_total(cls):
        return cls.instances
