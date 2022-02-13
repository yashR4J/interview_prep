def calculate(s:str) -> int:
    total = 0
    i, signs, op = 0, [1, 1], [1, -1]
    while i < len(s):
        c = s[i]
        if c.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            total += signs.pop() * int(s[start:i])
            continue
        if c in '+-(':
            signs.append(signs[-1] * op[c == '-'])
        elif c in ')':
            signs.pop()
        i += 1
    return total

if __name__ == '__main__':
    test_cases = [
        "1 + 1", " 2-1 + 2 ", "(1+(4+5+2)-3)+(6+8)"
    ]
    ans = [2, 3, 23]

    for i in range(len(test_cases)):
        assert calculate(test_cases[i]) == ans[i]