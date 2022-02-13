def solution(board, words):
    r = []
    for word in words:
        if canBoggle(board,word):
            r.append(word)
    return sorted(r)

def canBoggle(board, word, used = []):
    if len(word) == 0:
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i,j) not in used and board[i][j] == word[0]:
                if len(used)==0 or (abs(used[-1][0] - i)<=1 and abs(used[-1][1] - j)<= 1):
                    if canBoggle(board,word[1:],used + [(i,j)]):
                        return True
    return False     