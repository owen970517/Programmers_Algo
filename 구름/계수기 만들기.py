def solution(n, a, b, k):
    while 1 :
        if k== 0 :
            break
        k -= 1
        now = n - 1
        while now >= 0:
            if b[now] < a[now]:
                b[now] += 1
                break
            else:
                b[now] = 0
                now -= 1

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = int(input())
solution(n, a, b, k)
print(''.join(map(str,b)))