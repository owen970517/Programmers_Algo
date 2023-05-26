from itertools import permutations

n = int(input())
number = [i+1 for i in range(9)]
nPr = list(permutations(number,3))
for _ in range(n) :
    n,s,b = map(int,input().split())
    n = list(str(n))
    remove_cnt = 0
    for i in range(len(nPr)) :
        s_cnt,b_cnt = 0,0
        i -= remove_cnt
        for j in range(3) :
            n[j] = int(n[j])
            if n[j] in nPr[i] :
                if j == nPr[i].index(n[j]) :
                    s_cnt+= 1
                else :
                    b_cnt += 1
        if s_cnt != s or b_cnt !=b :
            nPr.remove(nPr[i])
            remove_cnt += 1
print(len(nPr))