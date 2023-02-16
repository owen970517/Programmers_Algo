A,B= map(str,input().split())
print(A,B)
diff = len(B)-len(A)
print(diff)
cnt = 0
# 두 문자열의 길이가 같은 경우
if diff == 0 :
    for i in range(len(A)) :
        if A[i] != B[i] :
            cnt += 1
# 다를 경우
else :
    pass
print(B[:7])