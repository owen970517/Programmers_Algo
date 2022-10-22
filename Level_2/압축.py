def solution(msg):
    answer = []
    dic = {}
    for i in range(ord('a'), ord('z')+1):
        dic[chr(i).upper()] = i-96
    start, end = 0, 0
    while end < len(msg):
        if msg[start:end+1] in dic:
            end += 1
        else:
            dic[msg[start:end+1]] = len(dic)+1
            answer.append(dic[msg[start:end]])
            start , end = end,end
    answer.append(dic[msg[start:end+1]])
    return answer

print(solution('ABABABABABABABAB'))
