result = []
li = {}
n = int(input())
s = list(map(int,input().split()))
for i in s :
    if i in li :
        li[i] += 1
    else :
        li[i] = 1
m = int(input())
h = list(map(int,input().split()))
for i in h :
    if i in li :
        result.append(li[i])
    else :
        result.append(0)
print(*result)