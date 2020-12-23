class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Liked List Class
    """
    instances = 0

    def __init__(self, head=None):
        self.head = head
        
        if self.head == None:
            self.length = 0
        else:
            self.length = 1

        LinkedList.instances+=1

    def __str__(self):
        dunder_str = ''
        current = self.head

        if current == None:
            return 'This is an empty Link List'

        while current is not None:
            dunder_str += f'{{ {current.value} }} -> '
            current = current.next
        
        dunder_str += f'NULL'

        return dunder_str

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node
        self.length+=1

    def includes(self, search_value) -> bool:
        current = self.head
        while current is not None:
            if current.value == search_value:
                return True
            current = current.next
        return False

    def create_collection(self)-> list:
        collection =[]
        current = self.head

        while current is not None:
            collection.append(current.value)
            current = current.next

        return collection

    def append(self, val) -> str:
        """[method will add a new node on to the end of the linked list]

        Args:
            val ([type]): [value of the new node]

        Returns:
            [str]: [__str__]
        """
        if not self.length:
            return "This method can not be used on an empty linked list"
        
        current = self.head
        while current is not None:

            if current.next is None:
                node = Node(val)
                current.next = node
                return self.__str__()
            
            current = current.next


    def insertBefore(self, search_val,new_value):
        pass

    def insertAfter(self, search_val,new_value):
        pass

    @classmethod
    def linked_lists_total(cls):
        return cls.instances


