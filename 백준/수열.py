# 연속된 부분 수열의 합 구할 시 투포인터 사용 
n,k = map(int,input().split())
sequence = list(map(int,input().split()))
end = 0
maxi = 1
for i in range(len(sequence)-(k-1)) :
    total = 0
    cnt = 0
    while 1 :
        if cnt == k :
            break
        total = sum(sequence[i:i+k])
        end += 1
        cnt += 1
    maxi = max(maxi,total)
print(maxi)

#     return answer
# print(solution([3, -2, -4, -9, 0, 3, 7 ,13 ,8, -3],5))