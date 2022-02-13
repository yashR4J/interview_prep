from typing import List

def minChocolate(height: List[int]) -> int:
    chocolates = [1 for _ in range(len(height))]
    for x in range(1, len(height)):
        if height[x] > height[x-1]:
            chocolates[x] = chocolates[x-1] + 1
    for x in range(len(height)-2, -1, -1):
        if height[x] > height[x+1]:
            chocolates[x] = max(chocolates[x], chocolates[x+1]+1)       
    return sum(chocolates)
    
if __name__ == '__main__':
    test_cases = [
        [1,10,8,7,6,5,11],
        [1,0,2],
        [1,2,2]
    ]
    ans = [18,5,4]

    for i in range(len(test_cases)):
        assert minChocolate(test_cases[i]) == ans[i]
