n = int(input())
budget = list(map(int,input().split()))
total_budget = int(input())

if sum(budget) < total_budget :
    print(max(budget))
else :
    start = 0 
    end = max(budget)
    while start <= end :
        mid = (start + end)//2
        total = 0
        for i in budget :
            if i > mid :
                total += mid
            else :
                total += i
        if total <= total_budget :
            start = mid + 1
        else :
            end = mid-1
    print(end)



# n,m = map(int,input().split())
# li = list(map(int,input().split()))
# start = 0
# end = max(li)
# while start <= end :
#     mid = (start+end)// 2
#     total = 0
#     for i in li :
#         if i > mid :
#             total += i-mid
#     if total >= m :
#         start = mid + 1
#     else :
#         end = mid - 1
# print(end)
