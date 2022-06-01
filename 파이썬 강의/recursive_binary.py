def solution(L, x, l, u):
    if l>u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L,x,l,mid-1)
    else :
        return solution(L,x,mid+1,u)

L =[2,3,5,6,9,11,15]
x = 6
l=0
u =len(L)-1
print(solution(L,x,l,u))




