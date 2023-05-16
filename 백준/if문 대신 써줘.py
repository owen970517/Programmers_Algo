import sys 

def bs() :
    res = 0
    start,end = 0,n-1
    while start <= end :
        mid = (start+end)//2
        if int(style[mid][1]) >= k :
            end = mid-1
            res = mid
        else :
            start = mid+1
    return res

input = sys.stdin.readline()
n,m = map(int,input().split())
style = []

for i in range(n) :
    s = list(map(str,input().split()))
    style.append(s)

for i in range(m) :
    k = int(input())
    print(style[bs()][0])


