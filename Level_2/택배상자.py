from collections import deque

def solution(order) :
    answer = 0
    main_belt = deque()
    for i in range(len(order)) :
        main_belt.append(i+1)
    sub_belt = deque()
    truck = []
    while main_belt : 
        if order[0] != main_belt[0] :
            if sub_belt and order[0] == sub_belt[-1] :
                order.pop(0)
                truck.append(sub_belt.pop())
            else :
                sub_belt.append(main_belt.popleft())
        else :
            truck.append(main_belt.popleft())
            order.pop(0)
    while sub_belt :
        if order[0] == sub_belt[-1] :
            order.pop(0)
            truck.append(sub_belt.pop())
        else :
            break
    answer = len(truck)
    return answer
# from collections import deque

# def solution(order) :
#     answer = 0
#     main_belt = deque()
#     sub_belt = deque()
#     truck = []
#     for i in range(len(order)) :
#         main_belt.append(i+1)
#     while main_belt :
#         if order[0] != main_belt[0] :
#             if sub_belt and order[0] == sub_belt[-1] :
#                 truck.append(sub_belt.pop())
#                 order.pop(0)
#             else :
#                 sub_belt.append(main_belt.popleft())
#         else :
#             truck.append(main_belt.popleft())
#             order.pop(0)
#     while sub_belt :
#         if order[0] == sub_belt[-1] :
#             truck.append(sub_belt.pop())
#             order.pop(0)
#         else :
#             break
#     answer = len(truck)
#     return answer
print(solution([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]))