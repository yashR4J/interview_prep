def minOperationsMaxProfit(customers, boardingCost, runningCost) -> int:
        # profits = []
        # peopleOnGondola = 0
        # rotations = 1
        # i = 0
        # x = 0
        r = (sum(customers) // 4) + 1
        extra = sum(customers) % 4
        lr_prof = ((4 * r) + extra) * boardingCost - r * runningCost
        if extra == 0:
            p_rot_prof = 4 * (r - 1) * boardingCost - (r - 1) * runningCost
        else:
            p_rot_prof = (4 * r) * boardingCost - (r - 1) * runningCost
        
        if max(lr_prof, p_rot_prof) < 0:
            return -1
        elif lr_prof > p_rot_prof:
            return r
        else:
            return r - 1
        # while i < len(customers):
        #     if customers[i] >= 4:
        #         peopleOnGondola += 4
        #         customers[i] -= 4
        #         x = 4
        #     else:
        #         peopleOnGondola += customers[i]
                
        #         i += 1
        #     profit = peopleOnGondola * boardingCost - rotations * runningCost
        #     profits.append(profit)
        #     print(f"Current profit is {peopleOnGondola} * ${boardingCost} - {rotations} * {runningCost} = {profit}")
        #     rotations += 1
        # max_profit = max(profits)
        # if max_profit >= 0:
        #     return profits.index(max_profit) + 1

x = [8,3]
y = 5
z = 6

print(minOperationsMaxProfit(x,y,z))