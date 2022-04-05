from typing import List
def maxProfit(l: List[int]) -> int:
    # bought, profit = -1, 0
    # for i in range(0, len(l)-1):
    #     if l[i] < l[i+1] and bought == -1:
    #         bought = l[i]
    #     elif l[i] > l[i+1] and bought != -1:
    #         profit += l[i] - bought
    #         bought = -1
    #     print(l[i], bought, profit)
    # if bought != -1: profit += l[-1] - bought
    # return profit
    profit, j = 0, 0
    for i in range(1, len(l)):
        if l[i-1] > l[i]: # decreasing sequence
           j = i
        elif i+1 == len(l) or l[i] > l[i+1]:
            profit += l[i] - l[j]
    return profit

    # if len(l) < 2: return 0
    # total, i = 0, 0
    # while i < len(l):
    #     if i == 0 and l[i+1] > l[i]:
    #         total -= l[i]
    #     elif i == len(l) and l[i-1] < l[i]:
    #         total += l[i]
    #     elif i+1 < len(l) and l[i+1] > l[i] and l[i-1] > l[i]:
    #         total -= l[i]
    #     elif i+1 < len(l) and l[i+1] < l[i] and l[i-1] < l[i]:
    #         total += l[i]
    #     i += 1
    # return total

    # total = 0
    # for i in range(0, len(l)-1):
    #     if l[i+1]-l[i] > 0:
    #         total += l[i+1]-l[i]
    # return total

    # profit, trough, peak = 0, -1, -1
    # if l[0] < l[1]:
    #     trough = l[0]
    # i = 1
    # while i < len(l)-1:
    #     if l[i] < l[i-1] and l[i] < l[i+1]:
    #         trough = l[i]
    #     elif l[i] > l[i-1] and l[i] > l[i+1]:
    #         peak = l[i]
    #     else:
    #         i += 1
    #         continue
    #     if trough != -1 and peak != -1:
    #         profit += peak - trough
    #         trough, peak = -1, -1
    #     i += 1
    # if l[len(l)-1] > l[len(l)-2] and trough != -1:
    #     profit += l[len(l)-1] - l[len(l)-2]
    # return profit

if __name__ == '__main__':
    test_cases = [
        [1,5,4,3,2,9],
        [1,2,3,4,5],
        [5,4,3,2,1]
    ]
    ans = [11, 4, 0]

    for i in range(len(test_cases)):
        try:
            assert maxProfit(test_cases[i]) == ans[i]
        except AssertionError:
            print(maxProfit(test_cases[i]), " is not equal to ", ans[i])