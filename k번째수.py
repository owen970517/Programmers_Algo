def solution(array, commands):
    answer = []
    for s in commands:
        i=s[0]-1
        j=s[1]
        k=s[2]-1
        new_array=array[i:j]
        new_array.sort()
        answer.append(new_array[k])
        array=array
    return answer

array =[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))