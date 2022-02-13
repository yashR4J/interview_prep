class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def traverseTree(t):
    if not t:
        return []
    queue = []
    queue.insert(0, t)
    ret = []
    while len(queue) > 0:
        node = queue.pop(len(queue)-1) # or queue.pop()
        ret.append(node.value)
        if node.left:
            queue.insert(0, node.left)
        if node.right:
            queue.insert(0, node.right)
    return ret

def largestValuesInTreeRows(t):
    res = []
    def helper(res, root, d):
        if not root:
            return
        if d == len(res):
            res.append(root.value)
        else:
            res[d] = max(res[d], root.value)

        helper(res, root.left, d+1)
        helper(res, root.right, d+1)
    helper(res, t, 0)
    return res

def digitTreeSum(t):
    arr = []
    def helper(arr, val, root):
        if not root: return
        if not root.left and not root.right: arr.append(int(val + str(root.value)))
        helper(arr, val + str(root.value), root.left)
        helper(arr, val + str(root.value), root.right)
        
    helper(arr, "", t)
    return sum(arr)