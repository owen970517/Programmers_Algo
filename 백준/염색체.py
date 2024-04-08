# 정규표현식 문제 
import re

t = int(input())
reg = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(t) :
    dic = {}
    now = input()
    print(reg.match(now))
    if reg.match(now) != None :
        print('Infected!')
    else :
        print('Good')
