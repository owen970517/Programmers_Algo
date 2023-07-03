import sys

input = sys.stdin.readline

n,m = map(int,input().split())
dic = dict()
for i in range(n+m) :
    if i < n :
        s = input()
        dic[s] = 1
    else :
        keyword = list(input().split(','))
        for i in keyword :
            if i in dic :
                dic[i] -= 1
                if dic[i] == 0 :
                    dic.pop(i)
        print(len(dic))