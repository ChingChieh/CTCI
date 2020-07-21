import LinkedList as ll

def delMiddleNode(mNode):
    mNode.value = mNode.next.value
    mNode.next = mNode.next.next

if __name__ == "__main__":
    llist = ll.LinkedList()
    llist.addMultiValue([2,5,4,7])
    node = llist.add(8)
    llist.addMultiValue([32,55,89])
    print(llist)
    delMiddleNode(node)
    print(llist)

