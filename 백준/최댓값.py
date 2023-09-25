li= []
m = 0
for i in range(9) :
    s = list(map(int,input().split()))   
    m = max(m,max(s))
    li.append(s)

for i in range(9) :
    if m in li[i] :
        print(m)
        print(i+1,li[i].index(m)+1)
        break
