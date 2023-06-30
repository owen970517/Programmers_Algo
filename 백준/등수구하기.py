n,new,p = map(int,input().split())
if n == 0 :
    print(1)
else :
    s = list(map(int,input().split()))
    s.append(new)
    s.sort(reverse=True)
    rank = s.index(new)+1
    if rank > p :
        print(-1)
    else :
        if n == p and new == s[-1] :
            print(-1)
        else :
            print(rank)
# n,new,p = map(int,input().split())
# rank = 1
# can =True
# if n == 0 :
#     print(1)
# else :
#     s = list(map(int,input().split()))
#     s.sort(reverse=True)
#     print(s)
#     for i in range(n) :
#         if s[i] > new :
#             rank += 1
#         if s[i] <= new :
#             if len(s) < p :
#                 s.insert(i,new)
            
#             else :
#                 can = False
#                 print(i,can)
#         if i < len(s)-1 and s[i] > new and s[i+1] < new :
#             s.pop(i+1)
#             s.append(new)
# print(can)
# if can :
#     print(rank)
# else :
#     print(-1)




