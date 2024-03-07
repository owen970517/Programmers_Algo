import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    note1 = list(map(int,input().split()))
    note1 = sorted(note1)
    m = int(input())
    note2 = list(map(int,input().split()))

    for i in note2 :
        start = 0
        end = n-1
        can =False
        while start <= end :
            mid = (start+end)// 2
            if note1[mid] == i :
                can = True
                break
            elif note1[mid] < i :
                start = mid+1
            else :
                end = mid-1
        if can :
            print(1)
        else :
            print(0)