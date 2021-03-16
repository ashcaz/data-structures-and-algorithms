class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        # if list is empty
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def _hash(self, key):

        sum = 0

        for ch in key:
            sum += ord(ch)

        primed = sum * 19

        index = primed % self.size

        return index

    def set(self, key, value):
        # Hash The key
        hashed_key_index = self._hash(key)

        # Determine if the bucket is empty
        # if it is empty create ll, otherwise add to the ll
        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].add((key, value))

    def get(self, requested_key):
        # Run our requested_key through the _hash method
        hashed_key_index = self._hash(requested_key)

        # assign the bucket to temp variable with the hashed index
        temp = self._buckets[hashed_key_index]

        # check if the index is empty or not
        if not temp:
            return None

        # assign something to the head of the linked list 'current'
        current = temp.head

        while current:
            if current.data[0] == requested_key:
                return current.data[1]

            current = current.next

    def contains(self, key):

        hashed_key_index = self._hash(key)

        if not self._buckets[hashed_key_index]:
            return False

        return True