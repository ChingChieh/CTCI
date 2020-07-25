import queue
import LinkedList as ll
COUNT = [10]
# At first glance I think I need to travel the tree level by level to create the array of linkedlist
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def build_tree(array, start, end):
    if start > end:
        return None
    mid = (end + start) // 2
    root = TreeNode(array[mid])
    root.right = build_tree(array, start, mid - 1)
    root.left = build_tree(array, mid + 1, end)

    return root

def createArray(start, end):
    array = []
    for i in range(start, end):
        array.append(i)
    return array


def print2DUtil(root, space = 0) :

    # Base case
    if (root == None) :
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.val)

    # Process left child
    print2DUtil(root.left, space)

def PreOrder(root, level, listOfLinkedList):
    if root:
        if listOfLinkedList == []:
            listOfLinkedList.append(ll.LinkedList())
        elif len(listOfLinkedList) <= level:
            listOfLinkedList.append(ll.LinkedList())
        listOfLinkedList[level].add(root.val)
        PreOrder(root.left, level + 1, listOfLinkedList)
        PreOrder(root.right, level + 1, listOfLinkedList)

# def bfs(root):
#     if root == None:
#         return None
#     q = queue.Queue()
#     q.put(root)
#     while not q.empty():
#         node = q.get()
#
#     pass

if __name__ == "__main__":
    array = createArray(1, 32)
    root = build_tree(array, 0, len(array) - 1)
    print2DUtil(root)
    l = []
    PreOrder(root, 0, l)
    for i in range(len(l)):
        print(l[i])


