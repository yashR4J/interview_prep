from typing import List

def lis(arr: List[int]):
    # O(n^2) algorithm
    lis = [1 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

if __name__ == '__main__':
    test_cases = [
        [9,3,5,3,4,5,9],
        [1,2,3,4,5],
        [9,8,7,6,5]
    ]
    ans = [4,5,1]

    for i in range(len(test_cases)):
        assert lis(test_cases[i]) == ans[i]

