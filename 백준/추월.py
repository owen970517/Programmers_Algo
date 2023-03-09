n = int(input())
enter = dict()
out = []
li = []
cnt = 0
for i in range(n*2) :
    s= input()
    if i < n :
        enter[s] = i
    else :
        out.append(s)
for i in range(n-1):
	for j in range(i+1, n):
		if enter[out[i]] > enter[out[j]] and out[i] not in li:
			li.append(out[i])
			break
print(len(li))

# n = int(input())
# enter = []
# out = []
# cnt = 0
# for i in range(n*2) :
#     s= input()
#     if i < n :
#         enter.append(s)
#     else :
#         out.append(s)
# for i in range(len(out)) :
#     if out == enter :
#         break
#     cnt += 1
#     idx = enter.index(out[i])
#     now = enter.pop(idx)
#     enter.insert(i,now)
# print(cnt)
