def balancedStringSplit(s: str) -> int:
    ans = counter = 0
    for x in s:
        if x == "R":
            counter += 1
        elif x == "L":
            counter -= 1
        else:
            raise Exception("Invalid Input")
        if counter == 0:
            ans += 1
    return ans
            
print(balancedStringSplit("RLRRLLRLRL")) # 4
print(balancedStringSplit("RLLLLRRRLR")) # 3
print(balancedStringSplit("LLLLRRRR"))   # 1