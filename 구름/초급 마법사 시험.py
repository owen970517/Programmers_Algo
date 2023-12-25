from collections import defaultdict, deque
# visited를 true,false로 사용하는 것이 아닌, 방문 배열로 처리하는 것을 생각하지 못했음
def bfs(x,y,k) :
    q = deque()
    q.append((x,y,0,k))
    visited = defaultdict(set)
    visited[k].add((x,y))
    print(visited)
    while q :
        x,y,time,k = q.popleft()
        if (x,y) == (r-1,c-1):
            return time
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx>=r or ny <0 or ny>=c or (nx,ny) in visited[k] :
                continue
            if maps[nx][ny] == '1' :
                if k>= 10 :
                    if 0<=nx+dx[i]<r and 0<=ny+dy[i]<c and maps[nx+dx[i]][ny+dy[i]] != '1' :
                        q.append((nx+dx[i],ny+dy[i],time+1,k-10))
                        visited[k-10].add((nx+dx[i],ny+dy[i]))
            else :
                q.append((nx,ny,time+1,k))
                visited[k].add((nx,ny))
    return -1


r,c,k = map(int,input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maps = [list(input()) for _ in range(r)]

print(bfs(0,0,k))
