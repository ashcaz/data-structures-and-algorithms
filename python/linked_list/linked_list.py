class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Liked List Class
    """
    instances = 0

    def __init__(self, head, values=None):
        self.head = head
        self.length = 1
        LinkedList.instances+=1

    # def __str__(self):
        # pass

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node
        self.length+=1
        # return self

    def includes(self, search_value) -> bool:
        current = self.head
        while current is not None:
            if current.value == search_value:
                return True
            current = current.next
        return False

    @classmethod
    def ll_total(cls):
        return cls.instances
    
    # def make_str(self):
    #     dunder_str = ''
    #     while self.next is not None:
    #         dunder_str = f'{self.head.value}'

