from itertools import combinations, permutations


t = int(input())
for i in range(t) :
    n = int(input())
    dic = dict([])
    cnt = 1
    for j in range(n) :
        s = list(map(str,input().split()))
        if s[1] not in dic :
            dic[s[1]] = [s[0]]
        else :
            dic[s[1]].append(s[0])
    for k in dic :
        if cnt == 0 :
            cnt += (len(dic[k])+1)
        else :
            cnt *= (len(dic[k])+1)
    print(cnt-1)