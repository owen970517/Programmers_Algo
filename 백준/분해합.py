n = int(input())
arr = []
for i in range(1,n+1) :
    sum = 0
    sum += i
    li = list(str(i))
    for j in li :
        sum +=int(j)
    if sum == n :
        arr.append(i)
        break
if len(arr) > 0 :
    print(arr[0])
else :
    print(0)