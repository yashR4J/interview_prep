from typing import List

def threeSumClosest(nums: List[int], target:int) -> int:    
    nums.sort()
    ret = None
    for i in range(len(nums) - 2): # leave two elements at the end
        if i > 0 and nums[i] == nums[i-1]: continue
        j, k = i+1, len(nums)-1 
        while j < k:
            temp = nums[i] + nums[j] + nums[k]
            if ret == None: ret = temp
            elif abs(target - ret) > abs(target - temp):
                ret = temp
            j += 1
            k -= 1
    return ret

if __name__ == '__main__':
    test_cases = [
        ([-1,2,1,-4], 1), ([0,0,0], 1)
    ]
    ans = [2, 0]

    for i in range(len(test_cases)):
        arg1, arg2 = test_cases[i]
        assert threeSumClosest(arg1, arg2) == ans[i]