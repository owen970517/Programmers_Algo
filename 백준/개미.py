n,m = map(int,input().split())
li = []
cnt = 0
left = list(input())
right = list(input())
T = int(input())
left = left[::-1]
meet = left+right
while 1 :
    if cnt == T :
        break
    if T == 0 :
        print(''.join(meet))
        break
    else :
        cnt += 1
        if cnt == 1 :
            meet[len(left)-1], meet[len(left)] = meet[len(left)] , meet[len(left)-1]
        else :
            for i in range(len(meet)-1) :
                print(meet[i],meet[i+1])
                if meet[i] in left and meet[i+1] in right :
                    meet[i],meet[i+1] = meet[i+1],meet[i]
                    if meet[i+1] == left[-1] :
                        break
print(''.join(meet))

















# print(li[0][::-1][-1] , li[1][0])
# meet_a = list(li[0][::-1])
# meet_b = list(li[1])
# print(meet_a,meet_b)
# cnt = 0

# if li[2] == 0 :
#     print(''.join(meet_a) + ''.join(meet_b))
# else :
#     while 1:
#         if int(li[2])== cnt :
#             break
#         print(cnt)
#         if cnt == 0 :
#             meet_a[2],meet_b[0] = meet_b[0],meet_a[2]
#             cnt += 1
#         else :
#             meet_a[cnt],meet_a[cnt+1] = meet_a[cnt+1],meet_a[cnt]
#             meet_b[cnt-1],meet_b[cnt] = meet_b[cnt],meet_b[cnt-1]
#             cnt += 1
# print(meet_a,meet_b)