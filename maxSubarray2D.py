# Python3 program to find maximum sum in Binary
# Tree such that no two nodes are adjacent.
 
# Binary Tree Node
 
""" utility that allocates a newNode
with the given key """
class newNode:
 
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

omap = dict()
def maxSum(node : newNode):
    global omap
    # base case
    if (not node): return 0
    if node in omap: return 0

    inc = node.data

    if (node.left):
        inc += maxSum(node.left.left) + maxSum(node.left.right)
    
    if (node.right):
        inc += maxSum(node.right.left) + maxSum(node.right.right)

    ex = maxSum(node.left) + maxSum(node.right)

    omap[node] = max(inc, ex)
    return max(inc, ex)

 
# Driver Code
if __name__ == '__main__':
    # root = newNode(1)
    # root.left = newNode(4)
    # root.right = newNode(2)
    # root.left.left = newNode(7)
    # root.left.right = newNode(5)
    # root.right.right = newNode(3)
    # root.left.right.left = newNode(8)
    # root.left.right.right = newNode(6)
    # root.left.right.left.right = newNode(9)
    root = newNode(5)
    root.left = newNode(4)
    root.left.left = newNode(1)
    root.left.left.left = newNode(6)
    root.right = newNode(3)
    root.right.right = newNode(4)
    root.right.right.right = newNode(9)

    root.right.left = newNode(10)
    root.right.left.left = newNode(3)
    root.right.left.left.left = newNode(2)
    root.right.right.left = newNode(3)
    root.right.right.left.left = newNode(7)
    root.right.right.left.left.left = newNode(9)

    root.right.right.right.left = newNode(6)
    root.right.right.right.left.left = newNode(4)
    root.right.right.right.left.left.right = newNode(1)

    print(maxSum(root))
    print([(x.data, omap[x]) for x in omap])
