def solution(want,number,discount) :
    answer = 0
    dic = dict()
    for i in range(len(want)) :
        dic[want[i]] = number[i]
    for i in range(len(discount)) :
        li = discount[i:i+10]
        buy= dict()
        for i in range(len(li)) :
            if li[i] not in buy :
                buy[li[i]] = 1
            else :
                buy[li[i]] += 1
        if buy == dic :
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))