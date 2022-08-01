import itertools

def solution(distance , rocks , n) :
    answer = 0
    rocks.sort()
    nCr = list(itertools.combinations(rocks, n))
    for i in nCr :
        for j in i :
            rocks = [x for x in int(j)]
            print(rocks)
    return answer

distance = 25
rocks = [2,14,11,21,17]
n = 2
print(solution(distance,rocks,n))