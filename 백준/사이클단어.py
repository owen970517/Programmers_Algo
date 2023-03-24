import sys
from collections import deque

N = int(sys.stdin.readline())
w_li = list()
for i in range(N):
    w_li.append(sys.stdin.readline().rstrip())

for i in range(N):
    dq = deque(w_li[i])
    while True:
        dq.append(dq.popleft())
        save = "".join(dq)
        if save == w_li[i]:
            break

        if save in w_li:
            idx = w_li.index(save)
            w_li.pop(idx)
            w_li.insert(idx, w_li[i])

w_li = set(w_li)
print(len(w_li))

# n = int(input())
# li = []
# dic = dict()
# cnt = 0
# for i in range(n) :
#     s = input()
#     li.append(s)
# dic[li[0]] = 1
# print(li[0].find(li[1][0]))
# for i in range(1, len(li)) :
#     if len(li[i-1]) != len(li[i]) :
#         cnt += 1
#     elif li[] 