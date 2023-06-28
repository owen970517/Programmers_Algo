from collections import deque

def bfs() :
    q = deque()
    q.append((0,0))
    visited[(0,0)] = 0
    while q :
        a,b = q.popleft() 
        if a == ea and b == eb :
            return visited[(a,b)]
        if (ma,b) not in visited :
            visited[(ma,b)] = visited[(a,b)] +1
            q.append((ma,b))
        if (a,mb) not in visited :
            visited[(a,mb)] =visited[(a,b)]+1
            q.append((a,mb))
        if (0,b) not in visited:
            visited[(0,b)] = visited[(a,b)] +1
            q.append((0,b))
        if (a,0) not in visited :
            visited[(a,0)] = visited[(a,b)] + 1
            q.append((a,0))
        if a <= mb-b and (0,a+b) not in visited :
            visited[(0,a+b)] = visited[(a,b)]+1
            q.append((0,a+b))
        if a > mb-b :
            na = a - (mb-b)
            nb = mb
            if (na,nb) not in visited :
                visited[(na,nb)] = visited[(a,b)] +1
                q.append((na,nb))
        if b <= ma-a and (a+b,0) not in visited :
            visited[(a+b,0)] = visited[(a,b)] +1
            q.append((a+b,0))
        if b > ma-a :
            na = ma
            nb = b - (ma-a)
            if (na,nb) not in visited :
                visited[(na,nb)] = visited[(a,b)] +1
                q.append((na,nb))
    
    return -1
ma,mb,ea,eb = map(int,input().split())
visited = {}
print(bfs())
