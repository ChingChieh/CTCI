import LinkedList as llist

def partition(ll, p):
    _ll_ = llist.LinkedList()
    current = ll.head
    while current:
        if current.value < p:
            _ll_.addToBeginning(current.value)
        else:
            _ll_.add(current.value)
        print(_ll_)
        current = current.next
    return _ll_

def partition_inPlace(node, p):
    head = None
    tail = None
    while node:
        nextNode = node.next
        if node.value < p:
            if head == None:
                head = node
                tail = node
            else:
                node.next = head
                head = node
        else:
            if tail == None:
                tail = node
                head = node
            else:
                tail.next = node
                tail = node
        node = nextNode
    tail.next = None
    return head
# 3 5 8 5 10 2 1
if __name__ == "__main__":
    ll = llist.LinkedList()
    ll.addMultiValue([3, 5, 8, 5, 10, 2, 1])
    ll.head = partition_inPlace(ll.head, 5)
    print(ll)
