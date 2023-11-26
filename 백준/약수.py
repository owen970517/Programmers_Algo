# n,m = map(int,input().split())
# measure = []
# for i in range(1,n+1) :
#     if n % i == 0 : 
#         measure.append(i)
# if len(measure) < m :
#     print(0)
# else :
#     print(measure[m-1])

n = int(input())

li = list(map(int,input().split()))
li.sort()

if len(li) > 1 :
    print(li[0] * li[-1])
else :
    print(li[0] ** 2)

