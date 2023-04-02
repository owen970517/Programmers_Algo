import itertools
def solution(n,m,k,u,v,l) :
    answer = ''
    belt = [u,v,l]
    li = []
    for i in range(len(belt)) : 
        nCr = list(set(itertools.combinations(belt[i],n)))
        for j in nCr :
            if sum(j) <= k :
                li.append(j)
    if len(li) == 0 :
        answer = -1        
    else :
        now  = min(li[0])
        if len(li) == 1 :
            answer = now
        else :
            for i in range(1,len(li)) :
                if min(li[i]) > now :
                    now  = li[i]
            answer = now
    return answer

print(solution(4,6,9,[1,2,3,1,1,2],[2,3,4,4,3,4],[3,3,3,3,1,2]))