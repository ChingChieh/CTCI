COUNT = [10]
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def checkBalence(root):
    if root == None:
        return 0, True
    leftLevel, leftResult = checkBalence(root.left)
    rightLevel, rightResult = checkBalence(root.right)
    if leftResult == False or rightResult == False or abs(leftLevel - rightLevel) > 1:
        return max(leftLevel, rightLevel) + 1, False
    return max(leftLevel, rightLevel) + 1, True

def buildBST(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = TreeNode(array[mid])
    root.left = buildBST(array, start, mid - 1)
    root.right = buildBST(array, mid + 1, end)
    return root

def searchBST(root, value):
    if root:
        if root.val == value:
            return root
        elif root.val > value:
            return searchBST(root.left, value)
        elif root.val < value:
            return searchBST(root.right, value)
    return None

def print2DUtil(root, space) :

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
# def preOrder(root, level):
#     if root:


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    b.left = c
    a.right = d
    level, result = checkBalence(a)
    print(result)
    array = []
    for i in range(63):
        array.append(i)
    root = buildBST(array, 0, len(array) - 1)
    print2DUtil(root, 0)
    node = searchBST(root, 58)
    node.right = TreeNode(512)
    node.right.left = TreeNode(333)
    print2DUtil(root, 0)
    level, result = checkBalence(root)
    print(result)

