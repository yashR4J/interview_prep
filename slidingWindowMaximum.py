from typing import List
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    # # Brute Force -- O(n*k)
    # return nums and [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
    # Deque Solution - O(n)
    queue, out = deque([]), []
    for i, n in enumerate(nums):
        while queue and nums[queue[-1]] < n:
            queue.pop() # replace lower values with greater values
        queue.append(i) # add index
        if queue[0] == i - k: queue.popLeft() # remove the lower window index
        if i >= k - 1: out.append(nums[queue[0]])
    return out
    

if __name__ == '__main__':
    test_cases = [
        ([1,3,-1,-3,5,3,6,7], 3),
        ([1], 1)
    ]
    ans = [[3,3,5,5,6,7], [1]]

    for i in range(len(test_cases)):
        arg1, arg2 = test_cases[i]
        # assert maxSlidingWindow(arg1, arg2) == ans[i]
        print(arg1, arg2, maxSlidingWindow(arg1, arg2))