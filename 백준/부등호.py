from itertools import permutations

def check(i,j,k) :
    if j == '<' :
        return i < k
    else :
        return i > k

k = int(input())
s = list(input().split())
nums = [0,1,2,3,4,5,6,7,8,9]
nCr = list(permutations(nums,k+1))
li = []

for i in nCr :
    for j in range(len(s)) :
        if not check(i[j],s[j],i[j+1])  :
            break
    else :
        li.append((''.join(map(str,i))))
        
print(li[-1])
print(li[0])
