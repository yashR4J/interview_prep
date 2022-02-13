class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None
    
def listSize(l):
    s = 1
    n = l
    while n.next: # find the size
        n = n.next
        s += 1
    return s

def removeKFromList(l: ListNode, k):
    # Given a singly linked list of integers l and 
    # an integer k, remove all elements from list l 
    # that have a value equal to k.
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l
        
def isListPalindrome(l):
    # Given a singly linked list of integers, determine 
    # whether or not it's a palindrome.
    
    # # Solution 1
    # arr = []
    
    # while l:
    #     arr.append(l.value)
    #     l = l.next
        
    # return arr[:] == arr[::-1]
    
    # # Solution 2
    
    if not l or not l.next:
        return True
        
    middle = listSize(l) // 2
  
    # [1, 2, n --> 2, 3] or [1, 3, 2, n --> 3, 1]
    n = l
    for i in range(middle): # get to the middle
        n = n.next
    if listSize(l) % 2:
        n = n.next
    
    r = n # reverse n
    m = r.next
    for _ in range(middle-1): # flip n
        m.next,r,m = r,m,m.next
    
    for _ in range(middle):
        if r.value != l.value:
            return False
        r = r.next
        l = l.next
    
    return True

def reverseLL(a):
    prev = None
    head = a
    while head:
        head.next, prev, head = prev, head, head.next
    return prev
    
def printLL(a):
    print("[", end="")
    while a:
        if a.next:
            print(a.value, end=", ")
        else:
            print(f"{a.value}]")
        a = a.next
    
def addTwoHugeNumbers(a, b):
    # You're given 2 huge integers represented by linked lists. 
    # Each linked list element is a number from 0 to 9999 that 
    # represents a number with exactly 4 digits. The represented 
    # number might have leading zeros. Your task is to add up 
    # these huge integers and return the result in the same format.
    
    a = reverseLL(a)
    b = reverseLL(b)
    
    # printLL(a)
    # printLL(b)
    
    ret = c = ListNode(0)
    
    carry = 0
    while a or b or carry:
        # print(f"{a.value if a else 0} + {b.value if b else 0} + {carry} = ", end="")
        _sum = a.value + carry if a else carry
        _sum += b.value if b else 0
        # print(_sum)
        carry = 0
        if _sum > 9999:
            _sum -= 10000
            carry = 1
        c.value = _sum
        c.next = ListNode(0)
        a = a.next if a else None
        b = b.next if b else None
        if not a and not b and not carry:
            c.next = None
        c = c.next

    a = reverseLL(a)
    b = reverseLL(b)
    ret = reverseLL(ret)
    
    return ret

def mergeTwoLinkedLists(l1, l2):
    # Given two singly linked lists sorted in non-decreasing 
    # order, your task is to merge them. In other words, return 
    # a singly linked list, also sorted in non-decreasing order,
    # that contains the elements from both original lists.
    
    # # Solution 1 - Merge Sort
    # if not l1 and not l2: return None
    
    # p1 = l1
    # p2 = l2
    # ret = p3 = ListNode(0)
    # while p1 and p2:
    #     if p1.value < p2.value:
    #         p3.value = p1.value
    #         p1 = p1.next
    #     else:
    #         p3.value = p2.value
    #         p2 = p2.next
    #     p3.next = ListNode(0) if p1 or p2 else None
    #     p3 = p3.next
    
    # while p1:
    #     p3.value = p1.value
    #     p1 = p1.next
    #     p3.next = ListNode(0) if p1 or p2 else None
    #     p3 = p3.next

    # while p2:
    #     p3.value = p2.value
    #     p2 = p2.next
    #     p3.next = ListNode(0) if p2 else None
    #     p3 = p3.next
    
    # return ret
    
    # # Solution 2
    if not l1: return l2;
    if not l2: return l1;
    
    if l1.value < l2.value:
        l1.next = mergeTwoLinkedLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLinkedLists(l2.next, l1)
        return l2

def reverseNodesInKGroups(l, k):
    # Given a linked list l, reverse its nodes k at a time and 
    # return the modified list. k is a positive integer that is 
    # less than or equal to the length of l. If the number of nodes 
    # in the linked list is not a multiple of k, then the nodes that 
    # are left out at the end should remain as-is.
    
    # You may not alter the values in the nodes - only the nodes 
    # themselves can be changed.
    
    if not l: return None
    if k > listSize(l): return l
        
    _next = prev = None
    head = l
    count = 0
    
    while head and count < k:
        _next = head.next
        head.next, prev = prev, head
        head = _next
        count += 1
        
    if _next: l.next = reverseNodesInKGroups(_next, k)
        
    return prev

def rearrangeLastN(l, n):
    # Given a singly linked list of integers l and a non-negative 
    # integer n, move the last n list nodes to the beginning of the 
    # linked list.
    
    if not l: return l
    
    llen, head, prev = 0, l, None
    while head:
        prev, head, llen = head, head.next, llen + 1
        
    # prev now points to the end of the original list
    
    if not 0 <= n < llen: return l
    
    curr, split, index = l, llen - n - 1, 0
    while index < split:
        curr, index = curr.next, index + 1
    
    prev.next = l # create circular list by pointing back to the original head
    new_head = curr.next # new_head is at the head of the split
    curr.next = None # remove circular connection from the split
    
    return new_head