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

# 3 5 8 5 10 2 1
if __name__ == "__main__":
    ll = llist.LinkedList()
    ll.addMultiValue([3, 5, 8, 5, 10, 2, 1])
    print(ll)
    print(partition(ll, 5))
