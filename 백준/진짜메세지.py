n = int(input())
for _ in range(n) :
    s = input()
    dic = dict()
    ans = True
    for i in range(len(s)) :
        if s[i] not in dic :
            dic[s[i]] = 1
        else :
            if dic[s[i]] > 3:
                dic[s[i]] -= 1
                continue
            else :
                dic[s[i]] += 1
            if dic[s[i]] == 3 :
                if i == len(s)-1 :
                    ans = False
                    break
                elif s[i] != s[i+1] :
                    ans = False
                    break
    if ans :
        print('OK')
    else :
        print('FAKE')

