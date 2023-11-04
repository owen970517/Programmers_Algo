import sys
input = sys.stdin.readline

n= int(input())

col = [0] * n
ans = 0

def check(x) :
    for i in range(x) :
        if col[x] == col[i] or abs(col[x]-col[i]) == x-i :
            return True
    return False

def bt(x):
  global ans

  # 가능한 경우
  if x==n:
    ans+=1
    return

  for i in range(n):
    # 현재 퀸의 위치
    col[x]=i 
    if not check(x):
      # 퀸이 공격할 수 없는 위치인 경우
      bt(x+1)
      
bt(0)
print(ans)