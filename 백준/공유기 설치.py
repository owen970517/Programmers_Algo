n,c = map(int,input().split())
li = []
for i in range(n) :
    x = int(input())
    li.append(x)

li.sort()
print(li)

start = 0
end = li[-1] - li[0]

while start<=end :
    mid = (start+end) // 2
