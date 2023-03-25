# n = int(input())
# new_name = input()
# li = []
# dis_li =[]
# cnt = 0
# for i in range(n) :
#     old_name = input()
#     if new_name == old_name :
#         cnt +=1
#         continue
#     else :
#         for j in new_name :
#             indexes = [idx+1 for idx, c in enumerate(old_name) if c == j]
#             li.append(indexes)
# print(li)
# for i in range(1,len(new_name)) :
#     print(i , i-1)
#     dis_li =[]
#     for j in li[i] :
#         for k in li[i-1] :
#             dis = j-k
#             dis_li.append(dis)
#     print(dis_li)



n = int(input())
new_name = input()
li = []
dis_li =[]
cnt = 0
for i in range(n) :
    old_name = input()
    if new_name == old_name :
        cnt +=1
        continue
    else :
        for j in new_name :
            dic = {}
            for k in range(len(old_name)) :
                if j == old_name[k] :
                    if j not in dic :
                        dic[j] = [k+1]
                    else :
                        dic[j].append(k+1)

            for a in dic :
                print(a)