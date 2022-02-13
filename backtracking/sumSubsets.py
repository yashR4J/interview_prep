def solution(arr, num):
    if num > sum(arr): return []
    subsets = []
    def helper(remaining, idx, seq, arr, subsets):
        if remaining == 0:
            subsets.append(seq)
            return None
        elif remaining > 0:
            for i in range(idx, len(arr)):
                if remaining-arr[i] >= 0:
                    helper(remaining-arr[i], i+1, seq + [arr[i]], arr, subsets)
    helper(num, 0, [], arr, subsets)
    
    dup_rem = []
    for subset in subsets:
        if subset not in dup_rem:
            dup_rem.append(subset)
    
    return dup_rem