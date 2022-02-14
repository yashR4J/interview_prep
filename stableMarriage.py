def stableMatching(n, menPref, womenPref):
    unmarried_men = list(range(n))
    menSpouse, womenSpouse = [None] * n, [None] * n
    nextManChoice = [0] * n
    
    while unmarried_men:
        man = unmarried_men[0]
        hisPref = menPref[man]
        woman = hisPref[nextManChoice[man]]
        herPref = womenPref[woman]
        currentHusband = womenSpouse[woman]
        
        if not currentHusband:
            menSpouse[man], womenSpouse[woman] = woman, man
            nextManChoice[man] += 1
            unmarried_men.pop(0)
        else:
            oldManRanking = herPref.index(currentHusband)
            newManRanking = herPref.index(man)
            if newManRanking < oldManRanking:
                menSpouse[man], womenSpouse[woman] = woman, man
                nextManChoice[man] += 1
                unmarried_men.pop(0)
                unmarried_men.append(currentHusband)
            else:
                nextManChoice[man] += 1
    
    return menSpouse