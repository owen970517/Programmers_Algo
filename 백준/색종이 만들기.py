n = int(input())
li = []
for i in range(n) :
    s = list(map(int,input().split()))
    li.append(s)
print(li)
for i in range(n) :
    print(li[i])
    if i <= n//2 -1 :
        print(li[i][:n//2])
        print(li[i][n//2::])
        li[i] = [li[i][:n//2],li[i][n//2::]]
        print(li[i])
    else :
        print(li[i][:n//2])
        print(li[i][n//2::])
print(li)