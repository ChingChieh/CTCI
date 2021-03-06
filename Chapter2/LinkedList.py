# Reference form https://github.com/careercup/CtCI-6th-Edition-Python
from random import randint

class LinkedListNode:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.addMultiValue(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        value = [str(x) for x in self]
        return " -> ".join(value)

    def __len__(self):
        counter = 0
        tmp = self.head
        while tmp:
            counter += 1
            tmp = tmp.next
        return counter

    def add(self, value):
        if self.head == None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def addToBeginning(self, value):
        if self.head == None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def addMultiValue(self, values):
        for v in values:
            self.add(v)

    def generate(self, n, minimum, maximum):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(minimum, maximum))
        return self

class DoublyLinkedList(LinkedList):

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value, None, self.tail)
        else:
            self.tail.next = LinkedListNode(value, None, self.tail)
            self.tail = self.tail.next
        return self

if __name__ == "__main__":
    llist = DoublyLinkedList().generate(10, 0, 30)
    print(llist)
    tmp = llist.tail
    while tmp != llist.head:
        print(tmp)
        tmp = tmp.prev
