# 처음으로 푼 방법 
# n,m =map(int,input().split())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# ans = A+B
# ans.sort()
# print(*ans)

# 투포인터로 푸는 방법 
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = []
start= 0
end = 0
while start < len(A) or end < len(B) :
    if start == len(A) :
        ans.append(B[end])
        end += 1
    elif end == len(B) :
        ans.append(A[start])
        start += 1
    else :
        if A[start] < B[end] :
            ans.append(A[start])
            start += 1
        else :
            ans.append(B[end])
            end += 1
print(ans)
