import sys

input = sys.stdin.readline
n,m = map(int,input().split())
poketmon = {}
for i in range(n) :
    s = input().rstrip()
    poketmon[i+1] = s
re_poketmon = dict(map(reversed,poketmon.items()))
for i in range(m) :
    question = input().rstrip()
    if question.isdigit() :
        print(poketmon[int(question)])
    else :
        print(re_poketmon[question])

