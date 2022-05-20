# import itertools


# li=[]
# arr=[3, 30, 34, 5, 9]
# new_arr=itertools.permutations(arr, len(arr))
# new_arr=list(new_arr)
# for i in new_arr:
#     num=('').join(map(str,i))
#     li.append(num)
# print(max(li))
# lambda x : x*3 은 num 값들을 3번 반복 
def solution(num):
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True) 
    answer=str(int(''.join(num)))
    return answer

num=[6,10,2]
print(solution(num))