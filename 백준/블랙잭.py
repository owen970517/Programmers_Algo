n,m = map(int,input().split())
li = list(map(int,input().split()))
arr = []
for i in range(len(li)) :
    for j in range(i+1,len(li)) :
        for k in range(j+1 , len(li)) :
            print(li[i],li[j],li[k])
            sum =li[i]+li[j]+li[k]  
            if sum <= m :
                arr.append(sum)
print(max(arr))