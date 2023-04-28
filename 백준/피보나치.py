f = [0, 1]
for i in range(2, 46):
    f.append(f[i-2] + f[i-1])

t = int(input())
for i in range(t) :
    n = int(input())
    answer = []
    for k in range(45,0,-1) :
        if f[k] <= n :
            answer.append(f[k])
            n -= f[k]
            if n == 0 :
                answer.sort()
                print(*answer)
                break
