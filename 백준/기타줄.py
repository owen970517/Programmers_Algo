n,m = map(int,input().split())
li = []
for i in range(m) :
    p,s = map(int,input().split())
    li.append((p,s))

p_sort = sorted(li,key=lambda x:x[0])
s_sort = sorted(li,key=lambda x:x[1])

mok , na = n // 6 , n % 6
a = p_sort[0][0] * (mok+1)
b = (p_sort[0][0] * mok) + (s_sort[0][1] * na)
c = s_sort[0][1] * n
print(min(a,b,c))