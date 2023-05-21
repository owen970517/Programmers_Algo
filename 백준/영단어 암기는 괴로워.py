import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
dic = dict()
for i in range(n) :
    s = input().rstrip()
    if len(s) >= m :
        if s not in dic :
            dic[s] = 1
        else :
            dic[s] += 1

dic = dict(sorted(dic.items(),key=lambda x:(-x[1], -len(x[0]),x[0])))
for i in dic :
    print(i)
