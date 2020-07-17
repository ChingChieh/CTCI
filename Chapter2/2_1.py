class ListNode:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        return

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def add_list_item(self, node):
        if self.head == None : self.head = node
        else : self.tail.next = node
        self.tail = node
        return 

    def list_length(self):
        count = 0
        current_node = self.head
        while current_node : 
            count += 1
            current_node =  current_node.next
        return count
    
    def print_list(self):
        current_node = self.head
        while current_node :
            print(str(current_node.data) + " -> ", end = '')
            current_node = current_node.next
        print()
        return 

def deleteDup(head):
    HastTable = set()
    previous = ListNode()
    while head :
        if not (head.data in HastTable) : 
            HastTable.add(head.data)
            previous = head
        else : 
            previous.next = head.next
        head = head.next
        print(HastTable)
    return head

if __name__ == "__main__":
    node = [ListNode() for i in range(20)]
    # node = []
    # for i in range(20):
    #     node.append(ListNode(i))
    Slist = SingleLinkedList()
    
    for i in range(0, 20):
        node[i].data = i
        Slist.add_list_item(node[i])

    node[4].data = 9
    node[7].data = 13
    node[3].data = 5

    Slist.print_list()
    deleteDup(Slist.head)
    Slist.print_list()
    #Slist.add_list_item(node)
    #Slist.add_list_item(node)
    #print(Slist.list_length())
