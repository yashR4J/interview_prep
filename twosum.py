from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Brute Force
    # for x in range(0, len(nums)-1):
    #     for y in range(x+1, len(nums)):
    #         if nums[x] + nums[y] == target:
    #             return [x, y]

    # O(n) soln using hashmap (dictionary)
    
    seen = {}
    for i, value in enumerate(nums):
        # Find what the other value must be
        remaining = target - nums[i]
        
        # Check if that value has been visited
        if remaining in seen:
            return [i, seen[remaining]]
        
        # Add to visited values
        seen[value] = i 

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([2,2], 4))