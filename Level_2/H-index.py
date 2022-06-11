def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)) :
        if i >= citations[i] :
            answer = i
            break
        elif i < citations[i] :
            answer = len(citations)


        

    return answer,citations

citations = [0,0,0,0,0]
print(solution(citations))