
from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    for x in nums1:
        try:
            index = nums2.index(x)
            res.append(x)
            nums2 = nums2[:index] + nums2[index+1:]
        except ValueError:
            pass
    return res

print(intersect([1,2,2,1], [2,2]))
print(intersect([4,9,5], [9,4,9,8,4]))