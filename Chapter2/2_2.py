import LinkedList as ll
class returnObject:
    def __init__(self, node, level):
        self.node = node
        self.level = level

def Kth_to_last_naive(llist, k):
    # Return type: ll.LinkedListNode
    l_size = len(llist)
    x = l_size - k
    node = llist.head
    for i in range(x):
        node = node.next
    return node

def Kth_to_last_recursive(node, k):
    # Return tpye: returnObject
    if node == None:
        return returnObject(None, -1)

    result = Kth_to_last_recursive(node.next, k)
    if result.level == k:
        node = result.node
        return returnObject(node, result.level)

    return returnObject(node, result.level + 1)

def Kth_to_last_runner(llist, k):
    # Return type: ll.LinkedListNode
    current = runner = llist.head
    for i in range(k):
        if runner == None:
            return None
        runner = runner.next
    while runner:
        current = current.next
        runner = runner.next
    return current

if __name__ == "__main__":
    llist = ll.LinkedList().generate(10, 0, 40)
    print(llist)
    print(len(llist))
    # print(Kth_to_last_naive(llist, 0))
    print(Kth_to_last_runner(llist, 4))
