t = int(input())

for i in range(t) :
    dic = {}
    n = list(input())
    for j in n :
        if j  != ' ':
            if j not in dic :
                dic[j] = 1
            else :
                dic[j] += 1
    ans = [k for k,v in dic.items() if max(dic.values()) == v]
    if len(ans) > 1 :
        print('?')
    else :
        print(ans[0])

