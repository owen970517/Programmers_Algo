n = int(input())
a = list(map(int,input().split()))
dp = [a[0]]

def binary_search(target) :
    start = 0
    end = len(dp) -1 

    while start <= end :
        mid = (start+end)//2

        if dp[mid] < target :
            start = mid + 1
        else :
            end = mid -1
    return start

for i in a :
    if dp[-1] < i :
        dp.append(i)
    else :
        now = binary_search(i)
        print(now,i)
        dp[now] = i
        print(dp)
print(len(dp))




