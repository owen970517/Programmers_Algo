def can_reach(x, y, t):
    if abs(x) + abs(y) > t or (x + y + t) % 2 != 0:
        return "NO"
    return "YES"
	
T = int(input())
arr = []
for _ in range(T):
    X, Y, N = map(int, input().split())
    print(can_reach(X,Y,N))