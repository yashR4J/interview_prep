import math

class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def hasPathWithGivenSum(t : Tree, s: int):
    def helper(t : Tree, _sum=0):
        if not t: return False
        _sum += t.value
        if not t.left and not t.right:
            if _sum == s: return True
            return False
        return helper(t.left, _sum) or helper(t.right, _sum)
    return helper(t) if t else s == 0

def height(t):
    if not t: return 0
    return max(height(t.left)+1, height(t.right)+1)

def isTreeSymmetric(t: Tree):
    d = [[] for _ in range(height(t)+1)]
    def helper(t: Tree, h=0):
        if not t: 
            d[h].append(None)
            return
        d[h].append(t.value)
        helper(t.left, h+1), helper(t.right, h+1)
    
    helper(t)
    for level in d:
        if level[:] != level[::-1]:
            return False
    return True

def findProfession(level, pos):
    if level == 1: return "Engineer"
    if findProfession(level-1, math.ceil(pos/2)) == 'Doctor':
        if pos % 2: return "Doctor"
        return "Engineer"
    
    if pos % 2: return 'Engineer'
    return "Doctor"

def countNodes(t):
    if not t: return 0
    return 1 + countNodes(t.left) + countNodes(t.right)
    
def kthSmallestInBst(t, k):
    count = countNodes(t.left)
    if k <= count:
        return kthSmallestInBst(t.left, k)
    elif k > count + 1:
        return kthSmallestInBst(t.right, k-count-1)
    return t.value

def equal(t1, t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False
    return t1.value == t2.value and equal(t1.left, t2.left) and equal(t1.right, t2.right)
        
def isSubtree(t1, t2):
    if not t1: return t1 == t2
    return equal(t1, t2) or isSubtree(t1.left, t2) or isSubtree(t1.right, t2)    

def restoreBinaryTree(inorder, preorder):
    if len(preorder) == 0: return None
    t = Tree(preorder.pop(0))
    left = inorder[:inorder.index(t.value)]
    right = inorder[inorder.index(t.value)+1:]
    t.left = restoreBinaryTree(left, preorder[:len(left)])
    t.right = restoreBinaryTree(right, preorder[len(left):])
    return t