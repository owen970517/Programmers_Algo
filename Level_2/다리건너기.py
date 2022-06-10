from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    dequeue = deque([0] * bridge_length)
    bridgesum = 0

    while dequeue:
        answer += 1
        t = dequeue.popleft()
        bridgesum -= t
        if truck_weights:
            if bridgesum + truck_weights[0] <= weight:
                start = truck_weights.pop(0)
                bridgesum += start
                dequeue.append(start)
            else:
                dequeue.append(0)

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length,weight,truck_weights))
