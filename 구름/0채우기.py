n = int(input())
li = []
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)
total = 0
col = [list(map(lambda x: x[i], li)) for i in range(n)]

for i in range(n) :
    for j in range(n) :
        if li[i][j] == 0 :
            total += sum(li[i])
            total += sum(col[j])
            break
print(total)