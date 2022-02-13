def findSubstrings(words, parts):
    parts = set(parts)
    ans = []
    for w in words:
        length = 5
        while length > 0:
            success=False
            for i in range(len(w) - length + 1):
                if w[i:i+length] in parts:
                    w = w[:i] + '[%s]' % w[i:i+length] + w[i+length:]
                    success=True
                    break
            if success: break
            length -= 1
        ans.append(w)
    return ans

if __name__ == '__main__':
    test_cases = [
        (["Apple", "Melon", "Orange", "Watermelon"], ["a", "mel", "lon", "el", "An"])
    ]
    ans = [["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"]]

    for i in range(len(test_cases)):
        arg1, arg2 = test_cases[i]
        assert findSubstrings(arg1, arg2) == ans[i]