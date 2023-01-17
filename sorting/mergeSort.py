from typing import List

def mergeSort(arr: List[int]) -> List[int]:
    def _mergeSort(arr: List[int], low:int, high:int) -> None:
        if low < high:
            mid = (low + high) // 2
            _mergeSort(arr, low, mid)
            _mergeSort(arr, mid + 1, high)
            _merge(arr, low, mid, high)

    def _merge(arr: List[int], low:int, mid:int, high:int) -> None:
        copy = [None for _ in arr]
        i, j, k = low, mid + 1, 0

        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                copy[k] = arr[i]
                i += 1
            else:
                copy[k] = arr[j]
                j += 1
            k += 1
        
        # add remaining elements in first half
        while i <= mid:
            copy[k] = arr[i]
            i += 1
            k += 1

        # add remaining elements in second half
        while j <= high:
            copy[k] = arr[j]
            j += 1
            k += 1
        
        # fix elements between {low, high + 1} in original array
        k = 0
        for i in range(low, high + 1):
            arr[i] = copy[k]
            k += 1
        
    _mergeSort(arr, 0, len(arr) - 1)
    return arr

if __name__ == '__main__':
    test_cases = [
        [1,5,3,2,7,4,6],
        list(range(100, 0, -1)),
        [1241,12,4,21,432,51,22,1,2,41,3]
    ]

    for test_case in test_cases:
        print(f"Unsorted array: {test_case}")
        assert sorted(test_case) == mergeSort(test_case)
        print(f"Sorted array: {test_case}")
