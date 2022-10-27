def solution(numbers) :
    answer = []
    for i in numbers :
        if i %2 ==0 :
            answer.append(i+1)
        else :
            bit = '0' + format(i,'b')
            zero_idx = bit.rfind("0")
            bit[zero_idx] = '1'
            bit[zero_idx+1] ='0'
            s = ''.join(bit)
            answer.append(int(s,2))
    return answer

print(solution([2,7]))


# def solution(numbers) :
#     answer = []
#     for i in numbers :
#         k = format(i , 'b').zfill(8)
#         while True :
#             cnt = 0
#             i += 1
#             j = format(i , 'b').zfill(8)
#             for z in range(len(k)) :
#                 if j[z] != k[z]  :
#                     cnt += 1
#             if cnt <= 2 :
#                 answer.append(i)
#                 break
#     return answer
