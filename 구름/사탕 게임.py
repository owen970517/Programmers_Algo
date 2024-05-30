t = int(input())
li = map(int,input().split())
goo = 0
f = 0
for i in li :
	if (i % 2 != 0 )  :
		goo += 1
	else :
		f+= 1

if goo == f :
	print('tie')
else :
	print(max(goo,f))