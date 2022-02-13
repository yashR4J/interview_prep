def reverse(x:int) -> int:
    neg = False
    if x < 0: 
        neg = True
        x = -x
    x = str(x)
    y = int(x[::-1])
    y = -y if neg else y
    if -2**31 <= y < 2**31: return y
    return 0

ipt = int(input("Please enter a numero: "))
print(reverse(ipt))

