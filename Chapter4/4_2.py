COUNT = [10]
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None

def build_min_binary_search_tree(array, root, start, end):
    # This function is full of bugs due to passing root.right/root.left to next recursion which is None!!!
    # root.val = array[mid] will cause ERROR!!!
    if start > end:
        return None
    mid = (end + start) // 2
    root.val = array[mid]
    print(root.val)
    root.right = build_min_binary_search_tree(array, root.right, mid + 1, end)
    root.left = build_min_binary_search_tree(array, root.left, start, mid - 1)

    return root
def build_tree(array, start, end):
    if start > end:
        return None
    mid = (end + start) // 2
    root = TreeNode(array[mid])
    root.left = build_tree(array, start, mid - 1)
    root.right = build_tree(array, mid + 1, end)

    return root

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

def PreOrderTraversal(node, level):
    if node:
        print(str(node.val) + " at:" + str(level))
        PreOrderTraversal(node.left, level + 1)
        PreOrderTraversal(node.right, level + 1)

def InOrderTraversal(node):
    if node:
        InOrderTraversal(node.left)
        print(node.val)
        InOrderTraversal(node.right)

if __name__ == "__main__":
    testArray = [1,2,3,4,5,6,7,8,9,10,11]
    # root = TreeNode()
    # root = build_min_binary_search_tree(testArray, root, 0, len(testArray) - 1)
    # print2DUtil(root, 0)
    tree = build_tree(testArray, 0, len(testArray) - 1)
    print2DUtil(tree, 0)
    print("Pre Order Traversal:")
    PreOrderTraversal(tree, 0)
    print("In Order Traversal:")
    InOrderTraversal(tree)

