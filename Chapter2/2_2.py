import LinkedListNode as LNode

def ReturnKthNode(head, k):
    if(head == None):
        return 0

    level = ReturnKthNode(head.next, k) + 1

    if(level == k):
        print("the kth node's data is " + str(head.data))

    return level


if __name__ == "__main__":
    node = [LNode.ListNode() for i in range(20)]
    # node = []
    # for i in range(20):
    #     node.append(ListNode(i))
    Slist = LNode.SingleLinkedList()

    for i in range(0, 20):
        node[i].data = i
        Slist.add_list_item(node[i])

    node[4].data = 9
    node[7].data = 13
    node[3].data = 5

    Slist.print_list()
    ReturnKthNode(Slist.head, 8)
    Slist.print_list()
