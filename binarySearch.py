
from typing import List

def binarySearch(array: List[int], target: int) -> int:
    def helper(array: List[int], low:int, high:int, target: int) -> int:
        if low <= high:
            mid = (low + high) // 2
            if array[mid] < target:
                return helper(array, mid + 1, high, target)
            elif array[mid] > target:
                return helper(array, low, mid - 1, target)
            else:
                return mid
        else:
            return -1
    return helper(array, 0, len(array) - 1, target) # search using low and high

if __name__ == '__main__':
    test_cases = [
        ([1,2,3,4,5],5),
        ([1,2,3,4,5],1),
        ([-1,1,3,5,6,7,8,11,21],3),
        ([-1,1,3,5,6,7,8,11,21],11)
    ]

    for test_case in test_cases:
        array, target = test_case
        assert binarySearch(array, target) == array.index(target)