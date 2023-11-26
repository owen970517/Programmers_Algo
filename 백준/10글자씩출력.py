# 간단한 풀이 방법 
# n = input()
# for i in range(0,len(n),10) :
#   print(n[i:i+10])

n = input()
cnt = 0
s = '' 
ans = []
for i in range(len(n)) :
    if cnt < 10 :
        s += n[i]
        cnt += 1
    if cnt == 10 :
        cnt = 0
        ans.append(s)
        s= ''
ans.append(s)
for i in ans :
    print(i)

