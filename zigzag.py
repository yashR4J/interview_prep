def zigzag(s:str, numRows:int) -> str:
    if numRows == 1: return s                                       # base case
    final = [''] * numRows                                          # create strings corresponding to numRows
    count = -1
    incrementer = True

    for idx, val in enumerate(s):
        if incrementer: count += 1                                 # going down, increment count; going up, decrement count
        else: count -= 1

        final[count] += val                                        # add value to respective row (count)
        if (idx != 0 and count == 0) or (count == numRows - 1):    # if count is at the top or bottom
            incrementer = not incrementer                          # flip the switch

    return ''.join(final)                                          # concatenate strings and return

print(zigzag("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR


# P A Y P A L I S H I R  I  N  G
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13

# P     A     H     N         
# A  P  L  S  I  I  G         
# Y     I     R               
# 0     4     8      12       (row 0)  
# 1  3  5  7  9  11  13       (row 1)
# 2     6     10              (row 2)

# P     ''      ''      ''         
# A  P  ''  ''  ''  ''  ''        
# Y     ''      ''        
