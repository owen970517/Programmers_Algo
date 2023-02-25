A,B= map(str,input().split())
li=[]
dis = len(B)-len(A)

for i in range(dis+1) :
    cnt = 0
    for j in range(len(A)) :
        if A[j] != B[j+i] :
            cnt += 1
    li.append(cnt)
print(min(li))    
