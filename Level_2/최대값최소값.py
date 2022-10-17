def solutions(s) :
    answer = ''
    result = []
    array = s.split()
    array = list(map(int,array))
    result.append(str(min(array)))
    result.append(str(max(array)))
    answer = ' '.join(result)
    return answer

print(solutions("-1 -2 -3 -4"))