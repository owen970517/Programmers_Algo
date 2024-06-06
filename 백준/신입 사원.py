import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t) :
    n = int(input())
    scores = []
    for _ in range(n) :
        a,b = map(int,input().split())
        scores.append((a,b))
    
    scores.sort(reverse=True)
    cnt = 1
    max_value = scores[0][1]
    for i in range(1,n) :
        if scores[i][1] > max_value :
            cnt += 1
        max_value = scores[i][1]
    print(cnt)