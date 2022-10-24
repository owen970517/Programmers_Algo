import re

def solution(arr) :
    answer = []
    new_array =[]
    for i in arr :
        i = re.split(r"([0-9]+)", i)
        new_array.append(i)
    array2 = sorted(new_array, key = lambda x:(x[0].upper(),int(x[1])))
    for i in array2 :
        i = ''.join(i)
        answer.append(i)
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))