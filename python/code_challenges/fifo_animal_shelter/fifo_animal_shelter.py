from code_challenges.stacks_and_queues.stacks_and_queues import (
    Queue,
    InvalidOperationError,
)


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal: str):
        """[Add the animal to the appropriate Queue]

        Args:
            animal (str): [either dog or cat]

        Raises:
            InvalidOperationError: [Will raise error when the animal provided is neither dog or cat]
        """
        # If animal isnt cat or dog return error
        if animal == "dog" or animal == "cat":
            # Check if animal is cat or dog
            # If dog
            if animal == "dog":
                # enqueue to dog queue
                self.dogs.enqueue(animal)
            # If cat
            elif animal == "cat":
                # enqueue to dog queue
                self.cats.enqueue(animal)
        else:
            raise InvalidOperationError("We only have cats and dogs at this shelter!")

    def dequeue(self, pref=None):
        """[removes animal from the appropriate Queue]

        Args:
            pref ([str], optional): [Which animal would you like to dequeue. Either dog or cat]. Defaults to None:str.

        Raises:
            InvalidOperationError: [Will raise error when the preference provided is neither dog or cat]

        Returns:
            [type]: [returns the dequeued node]
        """

        if pref == "dog" or pref == "cat":

            if pref == "dog":
                if self.dogs.front == None:
                    raise InvalidOperationError(
                        "Method not allowed on empty collection"
                    )
                    # dequeue to dog queue
                    return self.dogs.dequeue()
            elif pref == "cat":
                # dequeue to dog queue
                return self.cats.dequeue()

        return None
