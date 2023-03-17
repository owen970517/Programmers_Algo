n = int(input())
for _ in range(n) :
    s = input()
    dic = dict()
    ans = True
    for i in range(len(s)) :
        if s[i] not in dic :
            dic[s[i]] = 1
        else :
            dic[s[i]] += 1
            print(dic)
            if dic[s[i]] == 3:
                if i == len(s)-1 or s[i] != s[i+1]:
                    ans = False
                    break
                else :
                    dic[s[i]] = -1
    if ans :
        print('OK')
    else :
        print('FAKE')

