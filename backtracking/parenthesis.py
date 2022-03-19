import sys
from typing import List

def generateParenthesis(n: int) -> List[str]:
    def helper(l, r, p = ""):
        if l == r == 0: # all brackets have been added
            ret.append(p)
            return
        # add another opening bracket
        if l > 0: helper(l-1, r, p+'(')
        # add closing brackets if valid
        if r > l: helper(l, r-1, p+')')
        
    ret = []
    helper(n, n)
    return ret

if len(sys.argv) > 1:
    for x in range(len(sys.argv) - 1):
        print(generateParenthesis(int(sys.argv[x+1])))