n = int(input())
li = list(map(int,input().split()))
d = [0]*100
d[0] = li[0]
d[1] = max(li[0] , li[1])
print(d[1])
for i in range(2,n) :
    print(d[i-1],d[i-2]+li[i],d[i-2])
    d[i] = max(d[i-1] , d[i-2]+li[i])
    print(d[i])
print(len(d))
print(d[n-1])
