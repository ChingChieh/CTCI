from LinkedList import LinkedListNode as Node
from LinkedList import LinkedList as linkedlist

def delDuplicate_dict(llist):
    node = llist.head
    dictionary = {str(node):node}
    while node.next:
        if str(node.next) not in dictionary:
            dictionary[str(node.next)] = node.next
            node = node.next
        else:
            node.next = node.next.next

def delDuplicate_set(llist):
    node = llist.head
    seen = set([node.value])
    while node.next:
        if node.next.value in seen:
            node.next = node.next.next
        else:
            seen.add(node.next.value)
            node = node.next


if __name__ == "__main__":
    llist = linkedlist().generate(30, 10, 0)
    print(llist)
    delDuplicate_set(llist)
    print(llist)
