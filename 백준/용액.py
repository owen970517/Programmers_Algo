n = int(input())
li = list(map(int,input().split()))

start = 0
end = len(li)-1
dic = {}
# 처음 값을 int(1e9)로 했을 때 keyError가 발생했음 
k=abs(li[start]+li[end])
while start < end :
    now = li[start] + li[end] 
    if abs(now) <= k :
        k = abs(now)
        dic[k] = (li[start],li[end])
    if now < 0 :
        start += 1
    else :
        end -= 1

print(dic[k][0],dic[k][1])
