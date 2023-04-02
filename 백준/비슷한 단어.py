n = int(input())
li = []
cnt = 0
arr = []
for i in range(n) :
    s = input()
    li.append(s)

for k in range(len(li)) :
    for i in range(k+1,len(li)) :
        now = li[k]
        print(now,li[i])
        for j in range(len(li[i])) :
            if now[j] !=li[i][j]  :
                now = now.replace(now[j] , li[i][j])
        print(now)
        if now == li[i] :
            cnt +=1
print(arr)
print(cnt)
# now = 'abca'
# next = 'opqr'
# now = now.replace('a','o')
# print(now)

