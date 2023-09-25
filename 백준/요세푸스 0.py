n,k = map(int,input().split())
result = []
now = 0
li = [i for i in range(1,n+1)]
while 1 :
    if len(li) == 0 :
        break
    now += k-1 
    if now > len(li) :
        now %= len(li)
    result.append(str(li.pop(now)))
result = ', '.join(result)
print("<",result,">", sep="")