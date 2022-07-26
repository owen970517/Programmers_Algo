import itertools

def solution(clothes):
    closet = {}
    answer = 0
    result = 1
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]
    for i in closet.keys() :
        result =result*(len(closet[i])+1)
        answer = result -1
    return answer

clothes =[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))