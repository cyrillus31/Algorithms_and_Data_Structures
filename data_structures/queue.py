class Queue:
    "Implementation of a singly linked list as a queue data structure"

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    @classmethod
    def create_node(cls, value=None, next=None):
        "Creates a node of a singly linked list"

        class Node:
            def __init__(self, value=None, next=None):
                self.value = value
                self.next = next
        return Node(value, next)

    def enqueue(self, value):
        "Add a node to the tail node. Update tail pointer"
        self.length += 1
        enqueued_node = Queue.create_node(value) # node that is being added to the queue

        # if tail doesn't exists create head and tail nodes, and return None
        if not self.tail:
            self.head = self.tail = enqueued_node
            return
        
        # if tail exists enqueue the node
        self.tail.next = enqueued_node
        self.tail = enqueued_node

    def deque(self):
        "Remove the head node from the queue. Update head pointer. Return the value of the node being removed"
        # if head node does not exits return None
        if not self.head:
            return

        self.length -= 1
        dequed_value = self.head.value
        self.head = self.head.next
        return dequed_value

    def peek(self):
        "Look at the value of the head node without removing it"
        if self.head:
            return self.head.value


# testing
if __name__ == '__main__':
    q = Queue()

    q.enqueue(1)
    q.enqueue('second')
    q.enqueue(33)

    print(q.tail is q.head)
    print(f"Value of the head node is: {q.peek()}")
    print(f"Value of the dequed node is: {q.deque()}")
    print(f"Value of the head node is: {q.peek()}")


