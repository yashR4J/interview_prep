def combinationSum(arr, num):
    subsets = []
    
    def helper(remaining, arr, seq = []):
        if remaining == 0:
            if sorted(seq) not in subsets: subsets.append(seq)
            return None
        for i in range(len(arr)):
            if remaining-arr[i] >= 0:
                helper(remaining-arr[i], arr[i:], seq + [arr[i]])
            else:
                break
    
    helper(num, sorted(list(set(arr))))
    if len(subsets) == 0: return "Empty"
    subsets = ["(" + " ".join(map(str, x)) + ")" for x in subsets]
    return "".join(subsets)