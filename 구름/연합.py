# 유니온 파인드 알고리즘 사용 
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b
        
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for i in range(1,n+1) :
    parent[i] = i

for i in range(m) :
    s,e = map(int,input().split())
    graph[s].append(e)

for i in range(1,n+1) :
    for j in graph[i] :
        if i in graph[j] :
            union(i,j)

union_set = set()
for i in range(1,n+1) :
    union_set.add(find(i))

print(len(union_set))

