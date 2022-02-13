def commonChars(words):
    keyword = words[0]
    arr = words[1:]
    ans = []
    for char in keyword: # check if char is in each other word
        flag = True
        for idx, word in enumerate(arr):
            if char not in word:
                flag = False
                break
            else:
                arr[idx] = word.replace(char, "*", 1)
        if flag:
            ans.append(char)
    return ans

print(commonChars(["bella","label","roller"])) # ["e","l","l"]
print(commonChars(["cool","lock","cook"])) # ["c","o"]