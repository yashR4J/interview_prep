
def isValid(n):
    isbn = n[:9]
    isbn_last = n[-1]

    total_sum = 0
    for idx, val in enumerate(isbn):
        prod = (idx + 1) * int(val)
        total_sum += prod

    remainder = total_sum % 11

    if remainder == 10:
        return isbn_last == 'X'
    
    return remainder == int(isbn_last)

print(isValid('2222222224'))