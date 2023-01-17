def test():
    test_cases = [
        """
        2,
        7 3,
        1 2 3 4 5 6 7,
        5 10,
        7 7 7 7 7
        """
    ]
    ans = [18,5,4]

    for i in range(len(test_cases)):
        assert minChocolate(test_cases[i]) == ans[i]

"""
Bob rules kingdoms with consonants
Alice rules kingdoms with vowels
No one rules kingdoms with y
"""
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
noone = ['y', 'Y']
def centauri(k):
    if k[-1] in vowels:
        return k + " is ruled by Alice."
    elif not k.isalpha() or k[-1] in noone:
        return k + " is ruled by nobody."
    
    return k + " is ruled by Bob"

if __name__ == '__main__':
    kingdoms = int(input())
    
    for i in range(kingdoms):
        k = input().strip()
        print(f"Case #{i+1}: {centauri(k)}")