n,m = map(int,input().split())
medal =dict()
for i in range(n) :
    k,g,s,b = map(int,input().split())
    if k not in medal :
        medal[k] = [g,s,b]
medal = dict(sorted(medal.items()))
target = medal[m]
rank = 1
for i in medal :
    if i == m :
        continue
    if target < medal[i] :
        if rank >0 :
            rank += 1
            print(rank)
    elif target == medal[i] :
        rank=rank

print(rank)
