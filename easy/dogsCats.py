def dogsCats(l, df, cf, cfx):
    hungryDogs = l.count('D')
    for x in l:
        if x == 'D':
            df -= 1
            if df < 0: break
            cf += cfx
            hungryDogs -= 1
        elif x == 'C':
            cf -= 1
            if cf < 0: break
        else:
            raise Exception('Invalid Input')
    return 'YES' if hungryDogs == 0 else 'NO'

if __name__ == '__main__':
    no_cases = int(input())
    
    for i in range(no_cases):
        (_, dogFood, catFood, moreCatFood) = map(int, input().split(' '))
        order = input()
        print(f"Case #{i+1}: {dogsCats(order, dogFood, catFood, moreCatFood)}")