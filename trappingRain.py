from typing import List
def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    res = 0
    maxLeft, maxRight = 0, 0
    while left < right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft: maxLeft = height[left]
            else: res += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight: maxRight = height[right]
            else: res += maxRight - height[right]
            right -= 1
    return res

if __name__ == '__main__':
    test_cases = [  
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5],
        [0, 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 0]
    ]
    ans = [6, 9, 6]

    for i in range(len(test_cases)):
        assert trap(test_cases[i]) == ans[i]
    