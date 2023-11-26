# 2-> 10
# n = 1011
# print(list(str(n)))
# li = list(str(n))
# ans = 0
# for i in range(len(li)-1,-1,-1) :

#     if int(li[len(li)-1-i]) == 1 :
#         ans += pow(2,i)
# print(ans)

# 10 -> 2 

def decimal_to_binary(n):
    binary = 0
    i = 1
    while (n != 0): 
        remainder = n % 2
        n = n // 2
        binary = binary + remainder * i
        i = i * 10
    return binary