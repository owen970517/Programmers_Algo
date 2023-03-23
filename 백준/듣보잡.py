# dic =dict()
# li=[]
# for i in range(n+m) :
#     s = input()
#     if s not in dic :
#         dic[s] = 1
#     else :
#         dic[s] += 1

# for i in dic.items() :
#     if i[1] == 2 :
#         li.append(i[0])
# print(len(li))
# for i in sorted(li) :
#     print(i)
n,m = map(int,input().split())
a = set()
b=set()
for i in range(n+m) :
    s = input()
    if i < n :
        a.add(s)
    else :
        b.add(s)
answer = sorted(list(a&b))
print(len(answer))
for i in answer :
    print(i)