# def convert(n, q):
# 	t = ''
# 	if q>10:
# 		while n>0:
# 			n, mod = divmod(n, q)
# 			alphabet = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
# 			if mod >= 10:
# 				mod = alphabet[mod]
# 			t += str(mod)
# 	else:
# 		while n > 0:
# 			n, mod = divmod(n, q)
# 			t += str(mod)
# 	return t

# n,t = input().split()
# n = int(n)

# now = 2
# while 1 :
# 	k = convert(n,now)
# 	print(k)
# 	if ''.join(k[::-1]) == t :
# 		break 
# 	now += 1
# print(now)
dic = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def convert_to_base(n, base):
    res = ""
    while n > 0:
        n, mod = divmod(n, base)
        if mod >= 10:
            mod = dic[mod]
        res = str(mod) + res
    return res

def find_base(N, T):
    base = 2
    while base <= N:
        if convert_to_base(N, base) == T:
            return base
        base += 1

n,t = input().split()
n = int(n)
now = 2
while 1 :
	k = convert_to_base(n,now)
	if k == t :
		break 
	now += 1
print(now)