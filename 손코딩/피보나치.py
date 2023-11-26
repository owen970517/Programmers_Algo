import heapq
import math
import random

def loopFibo(n) :
    a,b,c = 0,1,0
    if n < 2 :
        return n
    else :
        for _ in range(2,n+1) :
            c = a+b
            a = b
            b = c

    return c

def recurFibo(n) :
    if n < 2 :
        return n
    else :
        return recurFibo(n-1) + recurFibo(n-2)

def dpFibo(n) :
    dp = [0] * (n+1)
    dp[1] = 1
    if n < 2 :
        return dp[n]
    else :
        for i in range(2,n+1) :
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
    
print(loopFibo(4))
print(recurFibo(4))
print(dpFibo(6))

def gcd(a,b) :# 최대공약수
    while (b != 0) :
        a,b = b , a%b
    return a

def lcm(a,b) : #최소공배수
    return (a*b) // gcd(a,b)

def factorial(n) :
    if n == 1 :
        return 1 
    else :
        return n * factorial(n-1)


print(factorial(4))

n ='asqwe12312'
print(n[::-1])
print(n.isdigit()) # 숫자확인
print(n.isalpha()) # 문자확인

def binary_search(li,target) :
    start = 0
    end = len(li)-1 
    while start<=end :
        mid = (start+end)//2
        if li[mid] == target :
            return mid
        elif li[mid] < target :
            start = mid+1
        else :
            end = mid-1
    return -1

print(math.floor(random.random()*10))

# 배열에서 K 번째로 큰 값을 찾기

# 내장 라이브러리 사용
def solution(nums,k) :
    li = []
    for i in nums :
        heapq.heappush(li,i)
        if len(li) > k :
            heapq.heappop(li)
    print(li)
    return heapq.heappop(li)

# 선택정렬 사용 
def selection_sort(arr):
    for i in range(len(arr)):
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def kth_largest_num(nums, k):
    sorted_nums = selection_sort(nums)
    return sorted_nums[k-1]

print(kth_largest_num([3, 2, 1, 5, 6, 4], 2))  # 5
print(solution([3, 2, 1, 5, 6, 4], 2))


#선택 정렬 
li = [7,3,2,9,4]

def selection_sort(li) :
    for i in range(len(li)) :
        min_idx = i
        for j in range(i+1,len(li)):
            if li[min_idx] > li[j] :
                min_idx = j
        li[i],li[min_idx] = li[min_idx], li[i]
    return li

#버블 정렬 
def bubble_sort(li) :
    for i in range(len(li)) :
        for j in range(len(li)-i-1) :
            if li[j] > li[j+1] :
                li[j],li[j+1] = li[j+1],li[j]
    return li

#삽입 정렬
def intersection_sort(li) :
    for i in range(1,len(li)) :
        now = li[i]
        j = i-1
        while j >= 0 and now < li[j] :
            # i or j+1
            li[i] = li[j]
            j -= 1

        li[j+1] = now
    return li

array = [3, 5, 2, 4, 1]

# 퀵 정렬 -> 이미 정렬되어 있는 배열에서 사용하는 것은 매우 비효율적
def quick_sort(li) :
    if len(li) <= 1 :
        return li
    mid = len(li)//2
    now = li[mid]

    a = [x for x in li if x < now]
    b = [x for x in li if x == now]
    c = [x for x in li if x > now]

    return quick_sort(a) + b + quick_sort(c)

#삽입 정렬 
def insert_sort(li) :
    for i in range(1,len(li)) :
        for j in range(i,0,-1) :
            if li[j] < li[j-1] : 
                li[j],li[j-1] = li[j-1],li[j]
    return li


print(selection_sort(li))
print(bubble_sort(li))
print(intersection_sort(li))
print(quick_sort(array))
print(insert_sort(li))
k = 9
print(li.index(k))


#배열에 0~10억까지 숫자가 있을 때 9억 6000이 몇번째 인덱스에 있는지 알려주는 함수를 만들어주세요.

# li = list(range(1, 1000000001))  
# target = 900006000
# print(li[900006000])
# # print(binary_search(li,target))

def isAnagram(str1,str2) :
    str1 = list(str1)
    str2 = list(str2)
    str1.sort()
    str2.sort()
    if str1 == str2 :
        return True
    
    return False

print(isAnagram('acdbe','ecabd'))
    
