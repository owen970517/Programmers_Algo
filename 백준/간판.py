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
            indexes = [idx for idx, c in enumerate(old_name) if c == j]
            li.append(indexes)
print(li)
for i in range(1,len(new_name)) :
    print(i , i-1)
    dis_li =[]
    for j in li[i] :
        for k in li[i-1] :
            dis = j-k
            dis_li.append(dis)
    print(dis_li)