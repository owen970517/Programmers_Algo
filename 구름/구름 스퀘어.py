# 처음에 우선순위큐를 사용하여 풀었을 때 실패
# from heapq import heappush


# n= int(input())

# li = []

# for _ in range(n) :
#     s,e = map(int,input().split())
#     heappush(li,(s,e))
#     cnt = 1
#     ne = li[0][1]

#     for i in range(1,len(li)) :
#         if li[i][0] == li[i][1] :
#             cnt += 1
#         else :
#             if ne+1 <= li[i][0] :
#                 cnt += 1
#     ne = li[i][1]

# print(cnt)

# 끝나는 시간을 기준으로 정렬 
n= int(input())

li = []

for _ in range(n):
    s, e = map(int, input().split())
    li.append((s, e))

li.sort(key=lambda x: (x[1], x[0]))

cnt = 1
ne = li[0][1]

for i in range(1,len(li)) :
	if ne+1 <= li[i][0] :
		cnt += 1
		ne = li[i][1]
print(cnt)