#
# Task: Write code that accepts an integer and prints the integers from 0 to that input integer in a spiral format. 
#
# For example, given an input of 39 the output would be:
#
#     20  21  22  23  24  25
#     19   6   7   8   9  26
# 39  18   5   0   1  10  27
# 38  17   4   3   2  11  28
# 37  16  15  14  13  12  29
# 36  35  34  33  32  31  30
#
# - - - X
# 5 0 1
# 4 3 2
#
import math


def spiral(num):
    numLen = len(str(num))
    size = math.floor(math.sqrt(num))+1
    rows = [['' for _ in range(size)] for _ in range(size)]
    i = j = int((size - 1) / 2)
    nums = [str(x) + (numLen-len(str(x)))*' ' for x in range(0, num+1)]
    rows[i][j] = nums.pop(0)
    counter = 0
    while len(nums) != 0:
        counter += 1
        end = False
        # go right
        for _ in range(counter):
            j += 1
            rows[i][j] = nums.pop(0) if len(nums) > 0 else numLen*' '
        
        # go down
        for _ in range(counter):
            i += 1
            rows[i][j] = nums.pop(0) if len(nums) > 0 else numLen*' '
        
        counter += 1
        # go left
        for _ in range(counter):
            j -= 1
            rows[i][j] = nums.pop(0) if len(nums) > 0 else numLen*' '
        
        # go left
        for _ in range(counter):
            i -= 1
            rows[i][j] = nums.pop(0) if len(nums) > 0 else numLen*' '
          
    for x in rows:
        print(' '.join(x))

spiral(39)
