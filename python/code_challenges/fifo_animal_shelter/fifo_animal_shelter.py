from code_challenges.stacks_and_queues.stacks_and_queues import Queue


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        pass
        # If animal isnt cat or dog return error
        # Check if animal is cat or dog
        # If dog
        # enqueue to dog queue
        # If cat
        # enqueue to dog queue

    def dequeue(self, pref=None):
        pass
        # If no pref
        # return None

        # If pref is dog
        # dequeue dog queue

        # If pref is cat
        # dequeue cat queue

        # return dequeued animal
