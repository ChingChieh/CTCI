import LinkedList as ll

def sumList(l1, l2):
    sumlist = ll.LinkedList()
    head1 = l1.head
    head2 = l2.head
    over10 = 0
    value = 0
    while head1 or head2 or over10:
        if head1:
            value += head1.value
            head1 = head1.next
        if head2:
            value += head2.value
            head2 = head2.next
        if over10:
            value += 1
        over10 = value // 10
        value = value % 10
        sumlist.add(value)
        value = 0

    return sumlist


if __name__ == "__main__":
    list1 = ll.LinkedList()
    list2 = ll.LinkedList()

    list1.addMultiValue([9, 7, 8])
    list2.addMultiValue([6, 8, 5])
    print("list1:" + str(list1))
    print("list2:" + str(list2))
    sumlist = sumList(list1, list2)

    print(sumlist)
