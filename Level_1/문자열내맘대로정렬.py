def solution(strings, n):
    answer = []
    strings.sort()
    answer = sorted(strings,key=lambda x : (x[n]))
    return answer

strings =["sun", "bed", "car"]
n =1
print(solution(strings,n))