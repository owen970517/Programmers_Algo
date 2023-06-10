# 코드 없이 풀이 과정을 보고 작성 
n,m=map(int,input().split())
order = list(map(int,input().split()))
cnt = 0
tab = []
for i in range(m) :
    if order[i] in tab :
        continue
    if len(tab) != n :
        tab.append(order[i])
    else :
        remain = order[i:]
        remove_idx = -1
        for j in range(len(tab)) :
            if tab[j] not in remain :
                k = tab[j]
                break
            now_idx = remain.index(tab[j])
            remove_idx = max(remove_idx,now_idx)
            k = remain[remove_idx]
        tab.remove(k)
        tab.append(order[i])
        cnt += 1
print(cnt)
