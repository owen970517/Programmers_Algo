def solution(genres,plays) :
    answer = 0
    dic ={}
    arr = []
    for i in range(len(genres)) :
        arr.append([genres[i],plays[i],i])
    arr = sorted(arr, key=lambda x: (x[0], -x[1], x[2])) 
    for i in arr :
        if i[0] not in dic :
            arr.remove(i)
            dic[i[0]] = i[1]
    dic = sorted(dic.items(),key=lambda x : (-x[1]))
        
    return answer,dic,arr

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))