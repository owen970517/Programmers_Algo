while True :
    n = input()
    gather = ['a','e','i','o','u']
    can = True
    cnt = 0
    consonant = 0
    vowel= 0
    if n == 'end':
        break
    for i in gather :
        if n.find(i) != -1 :
            cnt += 1
    if cnt < 1 :
        print(f'<{n}> is not acceptable.')
        continue
    if n[0] in gather :
        vowel += 1
    else :
        consonant += 1
    for i in range(1,len(n)) :
        if n[i] in gather :
            consonant=0
            vowel += 1
        else :
            vowel = 0
            consonant += 1
        if vowel == 3 or consonant == 3 :
            can=False
            break
    for i in range(1,len(n)) :
        if n[i-1] == n[i]:
            if n[i] != 'e' and n[i] != 'o' :
                can = False
                break
            else :
                can=True
                break
    if can :
        print(f'<{n}> is acceptable.')
    else :
        print(f'<{n}> is not acceptable.')
            
