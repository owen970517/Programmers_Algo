# 순열을 활용하여 품 
import itertools
def solution(k,dungeons) :
    answer = []
    cnt = 0
    nCr = list(itertools.permutations(dungeons,len(dungeons)))
    for i in nCr :
        now=k
        now_cnt=cnt
        for j in i :
            if now < j[0] :
                answer.append(now_cnt)
            else :
                now-=j[1]
                now_cnt +=1
            answer.append(now_cnt)
    return max(answer)

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k,dungeons))