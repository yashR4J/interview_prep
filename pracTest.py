from typing import List

def reverse(x: int) -> int:
    neg = True if x < 0 else False
    s = str(x) if x > 0 else str(-x)
    s = -1 * int(s[::-1]) if neg else int(s[::-1])
    return s if -2**31 <= s < 2**31 else 0

def arrayPairSum(nums: List[int]) -> int:
    nums = sorted(nums)
    sum = 0
    for i in range(0, len(nums), 2):
        sum += min(nums[i] , nums[i+1])
    return sum

if __name__ == '__main__':
    test_cases_a = [
        123, -123, 120
    ]
    ans_a = [321,-321,21]

    test_cases_b = [
        [1,4,3,2], [6,2,6,5,1,2]
    ]
    ans_b = [4, 9]
    
    for i in range(len(test_cases_a)):
        assert reverse(test_cases_a[i]) == ans_a[i]
    
    for i in range(len(test_cases_b)):
        assert arrayPairSum(test_cases_b[i]) == ans_b[i]