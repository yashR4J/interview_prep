def judgePoint24(nums):
    if len(nums) == 1 and abs(nums[0] - 24) <= 0.001: return True
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                base = [nums[k] for k in range(len(nums)) if i != k and j != k]
                if judgePoint24(base + [nums[i] + nums[j]]): return True
                if judgePoint24(base + [nums[i] - nums[j]]): return True
                if judgePoint24(base + [nums[j] - nums[i]]): return True
                if judgePoint24(base + [nums[i] * nums[j]]): return True
                if nums[j] != 0 and judgePoint24(base + [nums[i] / nums[j]]): return True
                if nums[i] != 0 and judgePoint24(base + [nums[j] / nums[i]]): return True
    return False