n = int(input())
li = []
for i in range(n) :
    s = input()
    s= sorted(s)
    new = ''.join(s)
    if new not in li :
        li.append(new)
    
print(len(li))