s = input()
result = s
for i in range(1, len(s)):
    for j in range(i+1, len(s)):
        result = min(result, s[:i][::-1] + s[i:j][::-1] + s[j:][::-1])
print(result)

# 내가 푼 풀이 
# s = input()
# li=[]
# cnt = 0
# while 1 :
#     idx = s.find(min(s))
#     if cnt < 2 :
#         li.append(s[:idx+1])
#         cnt += 1
#         s = s[idx+1::]
#     elif cnt == 2 :
#         li.append(s)
#         break
# print(li)

# print(li[0][::-1]+li[1][::-1]+li[2][::-1])  