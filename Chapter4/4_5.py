import Tree as t
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

if __name__ == "__main__":
    array = []
    for i in range(31):
        array.append(i)
    root = t.buildBFS(array, 0, len(array) - 1)
    t.print2DUtil(root, 0)
    print(checkBST(root))
    node = t.searchBST(root, 30)
    node.right = t.TreeNode(17)
    t.print2DUtil(root, 0)
    print(checkBST(root))
