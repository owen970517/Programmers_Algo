# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# w_li = list()
# for i in range(N):
#     w_li.append(sys.stdin.readline().rstrip())

# for i in range(N):
#     dq = deque(w_li[i])
#     while True:
#         dq.append(dq.popleft())
#         save = "".join(dq)
#         if save == w_li[i]:
#             break

#         if save in w_li:
#             idx = w_li.index(save)
#             w_li.pop(idx)
#             w_li.insert(idx, w_li[i])

# w_li = set(w_li)
# print(len(w_li))

n = int(input())
li = []
dic = dict()
cnt = 0
for i in range(n) :
    s = input()
    li.append(s)
print(sorted(li))
dic[li[0]] = [li[0]]
now = li[0]
for i in range(1,len(li)) :
    print(now,li[i])
    if len(now) == len(li[i]) :
        idx = now.find(li[i][0])
        print(idx)
        print(li[i][idx:] + li[i][:idx])
        if li[i] == now[idx:] + now[:idx] :
            dic[now].append(li[i])
        else :
            dic[li[i]] = [li[i]]
# for i in range(len(li)) :
#     now = li[i]
#     dic[now] = []
#     for j in range(i+1,len(li)) :
#         idx = now.find(li[j][0])
#         if li[j] == now[idx:] + now[:idx] :
#             dic[now].append(li[j])

print(dic)

# a= 'picture'
# print(a[3:]+a[:3])

