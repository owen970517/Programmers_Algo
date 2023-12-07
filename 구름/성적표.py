n,m= map(int,input().split())
dic = {}
for i in range(1,m+1) :
    dic[i] = []
for i in range(n) :
    c,s = map(int,input().split())
    dic[c].append(s)
for i in dic :
    if len(dic[i]) > 0 :
        dic[i] = (sum(dic[i]) / len(dic[i]) )
    else :
        dic[i] = 0
        
ans = [k for k,v in dic.items() if max(dic.values()) == v]
print(min(ans))
