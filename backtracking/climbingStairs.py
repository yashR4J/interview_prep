def solution(n, k):
    ret = []
    def recursiveHelper(n, k, seq, ret):
        if n == 0: ret.append(seq)
        else:
            for i in range(1, k+1):
                if n - i >= 0:
                    recursiveHelper(n-i, k, seq + [i], ret)
    recursiveHelper(n, k, [], ret)
    return ret