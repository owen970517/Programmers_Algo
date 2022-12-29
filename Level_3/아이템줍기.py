from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if len(rectangle) == 1 :
        answer = abs(characterX-itemX) + abs(characterY-itemY)
    return answer

print(solution([[1,1,5,7]],1,1,4,7))