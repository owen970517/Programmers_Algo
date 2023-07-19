from itertools import combinations


def solution(relation) :
    answer = 0
    candidates = []
    for i in range(1,len(relation)+1) :
        nCr = combinations(range(len(relation[0])),i)
        candidates.extend(nCr)
    unique = []
    for c in candidates:
        tmp = [tuple(item[key] for key in c) for item in relation] 
        if len(set(tmp)) == len(relation): 
            unique.append(c)
    Minimalism = set()
    for i in range(len(unique)) :
        for j in range(i+1,len(unique)) :
            if len(set(unique[i]) & set(unique[j])) == len(unique[i]) :
                Minimalism.add(unique[j])
    for i in Minimalism :
        if i in unique :
            unique.remove(i)
    answer = len(unique)
    return answer

print(solution([["100","ryan","music","2"]
                ,["200","apeach","math","2"]
                ,["300","tube","computer","3"]
                ,["400","con","computer","4"]
                ,["500","muzi","music","3"]
                ,["600","apeach","music","2"]]))