from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    ret = list()
    for i in range(len(nums) - 3): # leave three elements at the end
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i+1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j-1]: continue
            k = j + 1
            r = len(nums) - 1
            while k < r:
                temp = nums[i] + nums[j] + nums[k] + nums[r]
                if temp == target:
                    val = [nums[i], nums[j], nums[k], nums[r]]
                    val.sort()
                    if val not in ret: ret.append(val)
                    while k < r and nums[k] == nums[k+1]: k += 1
                    while k < r and nums[r] == nums[r-1]: r -= 1
                    k += 1
                    r -= 1
                elif temp < target: k += 1
                else: r -= 1
    return ret

if __name__ == "__main__":
    ipt = list(map(int, input("Please enter a list of integers: ").strip().split()))
    target = int(input("Please enter the target number: "))
    print(fourSum(ipt, target))
    

