#26
n= int(input())
d = [0] * (30001)

for i in range(2,n+1) :
    # 조건 4
    d[i] = d[i-1] +1
    # 조건 3
    if i %2 ==0 :
        d[i] = min(d[i] ,d[i//2] +1)
    #조건2
    if i %3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    #조건 1        
    if i % 5 == 0 :
        d[i] = min(d[i] , d[i//5] +1) 
print(d[n])