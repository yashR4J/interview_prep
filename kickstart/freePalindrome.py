from collections import deque

def free_palindrome(a, length) -> str:
    def palindrome(string) -> bool:
        return string == string[::-1]
    
    if length <= 4: return 'Possible'
    q1 = deque()
    q2 = deque()
    if a[0] == 'X':
        q1.append('1')
        q1.append('0')
    else:
        q1.append(a[0])
    
    FLAG = 0
    i = 0
    while i < length:
        while len(q1) != 0:
            b = q1.popleft()
            l = len(b) + 1
            if a[i]=='?':
                c = b + '0'
                if l <= 4:
                    q2.append(c)
                elif l == 5:
                    if not palindrome(c):
                        q2.append(c)
                else:
                    if not palindrome(c) and not palindrome(c[1:]):
                        q2.append(c[1:])

                c = b + '1';
                
                if l <= 4:
                    q2.append(c)
                elif l == 5:
                    if not palindrome(c):
                        q2.append(c)
                else:
                    if not palindrome(c) and not palindrome(c[1:]):
                        q2.append(c[1:])
            else:
                c = b + a[i];
                
                if l <= 4:
                    q2.append(c)
                elif l == 5:
                    if not palindrome(c):
                        q2.append(c)
                else:
                    if not palindrome(c) and not palindrome(c[1:]):
                        q2.append(c[1:])
        while len(q2) != 0:
            q1.append(q2.popleft())
        if len(q1) == 0:
            FLAG = 1
        i+=1
    
    return "IMPOSSIBLE" if FLAG == 1 else "POSSIBLE"
            
if __name__ == '__main__':
    test_cases = [
        '100???001', '100??'
    ]
    ans = ["IMPOSSIBLE", "POSSIBLE"]

    for i in range(len(test_cases)):
        output = free_palindrome(test_cases[i], len(test_cases[i]))
        try:
            assert output == ans[i]
        except:
            print(f"{output} not equal to {ans[i]}")
    
    no_cases = int(input())
    for i in range(no_cases):
        _len = int(input())
        string = input()
        print(f"Case #{i+1}: {free_palindrome(string, _len)}")

# def palindrome_exists(string, length):
#     if length < 5: return False
#     i = 0
#     while i <= length - 5:
#         j = i + 5
#         while j <= length:
#             substring = string[i:j]
#             if substring == substring[::-1]: return True
#             j += 1
#         i += 1
#     return False