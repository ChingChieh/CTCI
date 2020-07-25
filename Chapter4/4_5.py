COUNT = [10]
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildBFS(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = TreeNode(array[mid])
    root.left = buildBFS(array, start, mid - 1)
    root.right = buildBFS(array, mid + 1, end)

    return root

def checkBST(root):
    val = root.val
    if root.left == None and root.right == None:
        return True
    elif root.right == None:
        return root.val > root.left.val
    elif root.left == None:
        return root.val < root.right.val
    elif val > root.right.val or val < root.left.val:
        return False
    leftResult = checkBST(root.left)
    rightResult = checkBST(root.right)

    return leftResult and rightResult

def searchBST(root, value):
    if root:
        if root.val == value:
            return root
        elif root.val < value:
            return searchBST(root.right, value)
        elif root.val > value:
            return searchBST(root.left, value)
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
if __name__ == "__main__":
    array = []
    for i in range(31):
        array.append(i)
    root = buildBFS(array, 0, len(array) - 1)
    print2DUtil(root, 0)
    print(checkBST(root))
    node = searchBST(root, 30)
    node.right = TreeNode(17)
    print2DUtil(root, 0)
    print(checkBST(root))
