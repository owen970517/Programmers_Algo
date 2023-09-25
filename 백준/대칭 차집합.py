# 합집합 A | B
# 교집합 A & B
# 차집합 A - B
# 대칭 차집합 A ^ B

n,m = map(int,input().split())
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))

print(len(A^B))