import sys

wood =dict()
while 1 :
    s = sys.stdin.readline().rstrip()
    if s=='' :
        break
    if s not in wood :
        wood[s] = 1
    else :
        wood[s] += 1

sum = sum(wood.values())
wood = sorted(wood.items())
for i in wood :
    per = i[1]/sum * 100
    print(f'{i[0]} {per:.4f}')