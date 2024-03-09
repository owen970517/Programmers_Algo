l,w,h = map(int,input().split())
total = l*w*h
n = int(input())
cube =[]

for i in range(n) :
    x,k =map(int,input().split())
    cube.append((x,k))
cube.sort(key=lambda x:x[0],reverse=True)
total_cnt,ans =0,0
for v,n in cube :
    # 각 큐브의 부피가 8배씩 차이나기 때문
    total_cnt*=8
    # 지금 큐브의 한 변의 길이 
    now = 2**v
    # 현재 큐브로 채울 수 있는 최대 개수
    volume = (l//now) * (w//now) * (h//now) - total_cnt
    # 갖고 있는 큐브의 개수가 채울 수 있는 최대 개수보다 작을 수 있기 때문
    cnt = min(volume,n)
    ans += cnt
    total_cnt += cnt

if total_cnt == total :
    print(ans)
else :
    print(-1)


