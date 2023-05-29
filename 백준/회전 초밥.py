import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
plates = []
left , right = 0,k-1
for i in range(n) :
    plate = int(input())
    plates.append(plate)
ans = 0
while left < n :
    if right >= n :
        right -= n 
    if right < left :
        plate = plates[left:] + plates[:right+1]
    else :
        plate = plates[left:right+1]
    plate.append(c)
    plate = set(plate)
    ans = max(ans,len(plate))
    left+=1
    right += 1
print(ans)

# ans = []
# for i in range(len(plates)) :
#     if len(plates[i:i+k]) < k :
#         idx = k - len(plates[i:i+k])
#         new = plates[i:i+k] + plates[:idx]
#         new.append(c)
#         ans.append(len(list(set(new))))
#     else :
#         now = plates[i:i+k]
#         now.append(c)
#         ans.append(len(list(set(now))))

# print(max(ans))
