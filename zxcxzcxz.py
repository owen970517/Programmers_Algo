# x = int(input())
# n = int(input())
# sum = 0
# for _ in range(n) :
#     a,b = map(int,input().split())
#     sum += a*b
# if sum == x :
#     print('Yes')
# else :
#     print('No')
# byte = int(input())
# byte_4 = 'long int'
# cnt = byte // 4
# li = []
# answer =''
# while 1  :
#     if cnt == 1 :
#         li.append(byte_4)
#         break
#     else :
#         li.append('long')
#         cnt -= 1
# print(' '.join(li))
# import sys

# n, m = map(int, sys.stdin.readline().split())

# arr = [i for i in range(1, n + 1)]
# answer =''
# for _ in range(m):
#     i, j, k = map(int, sys.stdin.readline().split())
#     i, j, k = i - 1, j - 1, k - 1
#     arr = arr[:i] + arr[k:j + 1] + arr[i:k] + arr[j + 1:]
# for i in arr :
#     print(i,end=' ')
# dic ={
#     'A+' : 4.5,
#     'A0' : 4.0,
#     'B+' : 3.5,
#     'B0' : 3.0,
#     'C+' : 2.5,
#     'C0' : 2.0,
#     'D+' : 1.5,
#     'D0' : 1.0,
#     'F' : 0.0
# }
# sum = 0
# hak= 0
# for i in range(20) :
#     a,b,c = map(str,input().split())   
#     if c == 'P' :
#         continue
#     else :
#         sum += float(b) * dic[c]
#     hak += float(b)
# print(hak,sum)
# print(f'{sum/hak:.6f}')
# n = int(input())
# satan = 666
# number = 0
# while 1 :
#     if '666' in str(satan) :
#         number += 1
#     if number == n :
#         print(satan)
#         break
#     satan += 1
# a,b,c,d,e,f = map(int,input().split())
# x = (c*e - f*b)//(a*e-b*d)
# y=(c*d-f*a)//(b*d-e*a)
# print(x,y)    
# print(nx,ny)
# n,m = map(int,input().split())
# dic = dict()
# for i in range(n) :
#     if i+1 not in dic :
#         dic[i+1] = [0]
# for _ in range(m) :
#     i,j,k = map(int,input().split())
#     for z in range(i,j+1) :
#         dic[z].append(k)
# for i in dic :
#     print(dic[i][-1],end=' ')

# n,m = map(int,input().split())
# li = []
# for i in range(n) :
#     li.append(i+1)
# for _ in range(m) :
#     i,j = map(int,input().split())
#     li[i-1:j] = li[i-1:j][::-1]
# print(li)
# li=[]
# answer=[]
# for i in range(28) :
#     li.append(int(input()))
# for i in range(30) :
#     if (i+1) not in li :
#         answer.append(i+1)
# print(answer)

n,m = map(int,input().split())
li = []
cnt = 0
for i in range(n):
    s = list(input())
    for i in range(1,len(s)):
        prev = s[i-1]
        now = s[i]
        if prev == s[i]:
            if prev == 'B' :
                s[i] = 'W'
                cnt += 1
                print(s)
            else :
                s[i] = 'B' 
                cnt+=1
                print(s)
        print(cnt)
    li.append(s)
print(cnt)
