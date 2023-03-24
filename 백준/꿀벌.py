# work = input()
# dic = {
#     'Re' :0,
#     'Pt' :0,
#     'Cc':0,
#     'Ea' :0,
#     'Tb' :0,
#     'Cm' :0,
#     'Ex' :0,
# }
# work = work.split()
# cnt = 0
# for i in work :
#     if i in dic :
#         dic[i] += 1
#     else :
#         cnt += 1

# total=sum(dic.values())+cnt
# for i in dic :
#     print(f'{i} {dic[i]} {dic[i]/total:.2f}')
# print(f'Total {total} 1.00')
# 내가 푼 풀이 아래 와 입력하는 방식만 다르고 똑같은데 왜 틀린지 모르겠음 
import sys
dic = {
    'Re' :0,
    'Pt' :0,
    'Cc':0,
    'Ea' :0,
    'Tb' :0,
    'Cm' :0,
    'Ex' :0,
}
cnt = 0
lines = sys.stdin.readlines()
for line in lines:
    txt = list(line.split())
    for i in txt:
        if i in dic:
            dic[i] +=1
        else :
            cnt += 1
total = sum(dic.values()) +cnt
 
for i in dic:
    print(f'{i} {dic[i]} {dic[i]/total:.2f}')
 
print('Total', total, '1.00')
