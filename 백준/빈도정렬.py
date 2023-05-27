n,c = map(int,input().split())
li = list(map(int,input().split()))
dic=dict()
answer = []
for i in li :
    if i not in dic :
        dic[i]= 1
    else :
        dic[i] += 1
dic = dict(sorted(dic.items(), key=lambda x:x[1],reverse=True))
for i in dic :
    while 1 :
        if dic[i]== 0:
            break
        else :
            answer.append(i)
            dic[i] -= 1
print(*answer)