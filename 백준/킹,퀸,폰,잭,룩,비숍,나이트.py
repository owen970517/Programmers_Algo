have = list(map(int, input().split()))
chess = [1,1,2,2,2,8]
answer = []

for i in range(len(have)) :
    if have[i] <= chess[i] or have[i] > chess[i] :
        answer.append(chess[i]-have[i])

for i in answer :
    print(i , end=' ')
