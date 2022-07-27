import math 
def solution(w,h):
    answer =w*h - (w+h-math.gcd(w,h))
    return answer

w,h =8,12
print(solution(w,h))

""" 일차 함수를 만들어서 풀어보려고 했지만 12, 14번이 시간 초과가 나고 몇몇 케이스 또한 시간이 오래 걸리는 것을 확인
for i in range(1,w+1):
        # 일차 함수 
        y = -(h/w)*i + h
        answer +=int(y) """