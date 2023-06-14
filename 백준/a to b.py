#둘다 가능
from collections import deque

a,b = map(int,input().split())
q = deque()
q.append((a,1))
ans = 0
while q :
    x,cnt = q.popleft()
    if x>b :
        continue
    if x == b :
        ans = cnt
        break
    q.append((int(str(x)+'1'),cnt+1))
    q.append((x*2 , cnt+1))
print(ans)
if ans == 0 :
    print(-1)
else :
    print(ans)

from collections import deque

a,b = map(int,input().split())
q = deque()
q.append((a,1))
ans = 0
while q :
    x,cnt = q.popleft()
    if x>b :
        continue
    if x == b :
        print(cnt)
        break
    q.append((int(str(x)+'1'),cnt+1))
    q.append((x*2 , cnt+1))
else :
    print(-1)