import Tree as t
def checkBST(root, minValue, maxValue):
    if root == None:
        return True
    if (minValue != None and root.val < minValue) or (maxValue != None and root.val > maxValue):
        return False
    leftResult = checkBST(root.left, minValue, root.val)
    rightResult = checkBST(root.right, root.val, maxValue)
    if (leftResult == False) or (rightResult == False):
        return False
    return True

if __name__ == "__main__":
    array = []
    for i in range(31):
        array.append(i)
    root = t.buildBFS(array, 0, len(array) - 1)
    t.print2DUtil(root, 0)
    print(checkBST(root, None, None))
    node = t.searchBST(root, 14)
    node.val = 500
    t.print2DUtil(root, 0)
    print(checkBST(root, None, None))
