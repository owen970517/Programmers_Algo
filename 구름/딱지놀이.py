n = int(input())
ans = []
for i in range(n) :
    A_dic = {
        1:0,
        2:0,
        3:0,
        4:0
    }
    B_dic = {
        1:0,
        2:0,
        3:0,
        4:0
    }
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in A[1::] :
        A_dic[i] += 1
    for i in B[1::] :
        B_dic[i] += 1
    if A_dic[4] != B_dic[4] :
        if A_dic[4] > B_dic[4] :
            ans.append('A')
        else :
            ans.append('B')
    elif A_dic[4] == B_dic[4] and A_dic[3] != B_dic[3]:
        if A_dic[3] > B_dic[3] :
            ans.append('A')
        else :
            ans.append('B')
    elif A_dic[4] == B_dic[4] and A_dic[3] == B_dic[3] and A_dic[2] != B_dic[2]:
        if A_dic[2] > B_dic[2] :
            ans.append('A')
        else :
            ans.append('B')
    elif A_dic[4] == B_dic[4] and A_dic[3] == B_dic[3] and A_dic[2] == B_dic[2] and A_dic[1] != B_dic[1]:
        if A_dic[1] > B_dic[1] :
            ans.append('A')
        else :
            ans.append('B')
    elif A_dic[4] == B_dic[4] and A_dic[3] == B_dic[3] and A_dic[2] == B_dic[2] and A_dic[1] == B_dic[1]:
        ans.append('D')
for i in ans :
    print(i)
print()